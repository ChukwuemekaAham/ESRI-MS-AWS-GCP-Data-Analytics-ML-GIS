import base64
import boto3
import json
import os
from decimal import *

#os.environ['kafka_flag_topic']

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    dynamo_table=dynamodb.Table(os.environ["dynamodb_table"])

    for partition_key, partition_value in event['records'].items():
        for record_value in partition_value:
            data = json.loads(base64.b64decode(record_value['value']), parse_float=Decimal)
            dynamo_table.put_item(
            Item={
                "Account_Id": data["Account_Id"],
                "Transaction_Id": data["Transaction_Id"],
                "Transaction_Date": data["Transaction_Date"],
                "Flag_Date": data["Flag_Date"],
                "Transaction_Amount": data["Transaction_Amount"],
                "Customer_Name": data["Customer_Name"],
                "Merchant_Type": data["Merchant_Type"],
                "Transaction_Type": data["Transaction_Type"]
                 }
            )
