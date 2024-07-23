import boto3,logging
import json, os
import urllib3
http = urllib3.PoolManager()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

stepFunction = boto3.client('stepfunctions')

def lambda_handler(event, context):
    logger.info(event)

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    event_name = event['Records'][0]['eventName']
    logger.info(bucket_name)
    logger.info(file_key)
    logger.info(event_name)

    input= {
    'bucket_name': bucket_name,
    'file_key': file_key
    }
    if (bucket_name == os.environ['dataBucket']) and (event_name == 'ObjectCreated:Put'):
        response = stepFunction.start_execution(
        stateMachineArn=os.environ['batchProcessingStep'],
        input = json.dumps(input, indent=4)
        )
        logger.info(response)