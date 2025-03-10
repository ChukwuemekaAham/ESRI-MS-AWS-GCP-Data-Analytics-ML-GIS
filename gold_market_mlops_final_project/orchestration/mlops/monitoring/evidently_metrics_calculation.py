import datetime
import time
import random
import logging 
import uuid
import pytz
import pandas as pd
import io
import psycopg
import joblib

# from prefect import task, flow

from evidently.report import Report
from evidently import ColumnMapping
from evidently.metrics import ColumnDriftMetric, DatasetDriftMetric, DatasetMissingValuesMetric

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

SEND_TIMEOUT = 10
rand = random.Random()

create_table_statement = """
drop table if exists dummy_metrics;
create table dummy_metrics(
	timestamp timestamp,
	prediction_drift float,
	num_drifted_columns integer,
	share_missing_values float
)
"""

reference_data = pd.read_csv('./data/reference.csv')
with open('models/ln_reg.bin', 'rb') as f_in:
	model = joblib.load(f_in)

raw_data = pd.read_csv('./data/gold-cleaned-2024-09-02.csv')

raw_data['Date'] = pd.to_datetime(raw_data['Date'])

begin = datetime.datetime(2000, 7, 30, 0, 0)

num_features = ['Open','High','Low']
feature = raw_data[num_features].fillna(0)

cat_features = None
target= None
column_mapping = ColumnMapping(
    prediction='prediction',
    numerical_features=num_features,
    categorical_features=cat_features,
    target=target
)

report = Report(metrics = [
    ColumnDriftMetric(column_name='prediction'),
    DatasetDriftMetric(),
    DatasetMissingValuesMetric()
])

# @task
def prep_db():
	with psycopg.connect("host=postgres port=5432 user=postgres password=postgres", autocommit=True) as conn:
		res = conn.execute("SELECT 1")
		if len(res.fetchall()) == 0:
			conn.execute("create database test;")
		with psycopg.connect("host=postgres port=5432 dbname=postgres user=postgres password=postgres") as conn:
			conn.execute(create_table_statement)

# @task
def calculate_metrics_postgresql(curr, i):
	current_data = raw_data[(raw_data.Date >= (begin + datetime.timedelta(i))) &
		(raw_data.Date < (begin + datetime.timedelta(i + 1)))]

	#current_data.fillna(0, inplace=True)
	current_data['prediction'] = model.predict(feature)

	report.run(reference_data = reference_data, current_data = current_data,
		column_mapping=column_mapping)

	result = report.as_dict()

	prediction_drift = result['metrics'][0]['result']['drift_score']
	num_drifted_columns = result['metrics'][1]['result']['number_of_drifted_columns']
	share_missing_values = result['metrics'][2]['result']['current']['share_of_missing_values']

	curr.execute(
		"insert into dummy_metrics(timestamp, prediction_drift, num_drifted_columns, share_missing_values) values (%s, %s, %s, %s)",
		(begin + datetime.timedelta(i), prediction_drift, num_drifted_columns, share_missing_values)
	)

# @flow
def batch_monitoring_backfill():
	prep_db()
	last_send = datetime.datetime.now() - datetime.timedelta(seconds=10)
	with psycopg.connect("host=postgres port=5432 dbname=postgres user=postgres password=postgres", autocommit=True) as conn:
		for i in range(0, 27):
			with conn.cursor() as curr:
				calculate_metrics_postgresql(curr, i)

			new_send = datetime.datetime.now()
			seconds_elapsed = (new_send - last_send).total_seconds()
			if seconds_elapsed < SEND_TIMEOUT:
				time.sleep(SEND_TIMEOUT - seconds_elapsed)
			while last_send < new_send:
				last_send = last_send + datetime.timedelta(seconds=10)
			logging.info("data sent")

if __name__ == '__main__':
	batch_monitoring_backfill()
