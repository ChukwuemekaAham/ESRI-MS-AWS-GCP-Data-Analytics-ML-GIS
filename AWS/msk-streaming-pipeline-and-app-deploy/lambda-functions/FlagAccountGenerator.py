import boto3
import datetime
import json
import random
from random import randint
import os

import time

from kafka import KafkaProducer


def get_acc_number():
    num = randint(1000000001,1000000010)
    return num

def get_usage_date():
    return datetime.datetime.now().isoformat()

msk = boto3.client("kafka")

def lambda_handler(event, context):
    cluster_arn = os.environ["mskClusterArn"]
    response = msk.get_bootstrap_brokers(
            ClusterArn=cluster_arn
        )
    producer = KafkaProducer(security_protocol="PLAINTEXT",bootstrap_servers=response["BootstrapBrokerString"],value_serializer=lambda x: x.encode("utf-8"))

    for _ in range(1, 5):
        data = json.dumps({
            "Account_Id": get_acc_number(),
            "Flag_Date": get_usage_date()
        })

        producer.send(os.environ["kafka_topic"], value=data)
        time.sleep(1)
