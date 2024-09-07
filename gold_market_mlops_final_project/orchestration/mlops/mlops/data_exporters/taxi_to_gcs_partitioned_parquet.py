import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/clear-router-390022-c9dc0b907401.json'

bucket_name = 'demo-bucket390022'

project_id = 'clear-router-390022'

table_name = 'nyc_taxi_data'

root_path = f'{bucket_name}/{table_name}'


@data_exporter
def export_data(data, *args, **kwargs):
    
    data['tpep_pickup_date'] = data['tpep_pickup_datetime'].dt.date
    # Specify your data exporting logic here
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['tpep_pickup_date'],
        filesystem=gcs
    )