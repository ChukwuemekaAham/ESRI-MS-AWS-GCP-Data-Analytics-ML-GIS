import boto3
import datetime
import json
import os
import random
from random import randint
import names

import time

from kafka import KafkaProducer

txn_locations = ['Grocery_Store', 'Gas_Station', 'Shopping_Mall', 'City_Services', 'HealthCare_Service', 'Food and Beverage', 'Others']
txn_type=['Online', 'In Store']

def get_acc_number():
    num = randint(1000000001,1000000020)
    return num

def get_cust_name():
    return random.choice()

def generate_customers():
    return names.get_full_name()

def get_usage_amount():
    a = round(random.randint(100, 10000)* random.random(),2)
    return a

def get_txn_id():
    txnid=''.join(random.choice('0123456789ABCDEF') for i in range(16))
    return txnid

def get_usage_date():
    return datetime.datetime.now().isoformat()

msk = boto3.client("kafka")

def lambda_handler(event, context):
    cluster_arn = os.environ["mskClusterArn"]
    response = msk.get_bootstrap_brokers(
            ClusterArn=cluster_arn
        )
    producer = KafkaProducer(security_protocol="PLAINTEXT",bootstrap_servers=response["BootstrapBrokerString"],value_serializer=lambda x: x.encode("utf-8"))

    #producer = KafkaProducer( security_protocol="PLAINTEXT",bootstrap_servers=os.environ["bootstrap_servers"], value_serializer=lambda x: x.encode("utf-8"))

    for _ in range(1, 11):
        #data = json.dumps(f'"account_id":"{get_acc_number()}","customer_name":"{generate_customers()}","transaction_loc:"{random.choice(txn_locations)}","Transaction_id":"{get_txn_id()}","Transaction_type":"{random.choice(txn_type)}","Transaction_amount":"{get_usage_amount()}",Transaction_date":"{get_usage_date()}"')
        data = json.dumps({
            "Account_Id": get_acc_number(),
            "Customer_Name": generate_customers(),
            "Merchant_Type": random.choice(txn_locations),
            "Transaction_Id": get_txn_id(),
            "Transaction_Type": random.choice(txn_type),
            "Transaction_Amount": get_usage_amount(),
            "Transaction_Date": get_usage_date()
        })

        producer.send(os.environ["kafka_topic"], value=data)
        time.sleep(1)
