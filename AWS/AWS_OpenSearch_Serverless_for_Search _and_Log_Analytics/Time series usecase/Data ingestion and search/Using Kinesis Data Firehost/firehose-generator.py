import sys, getopt
import datetime
import json
import boto3
import random

def get_data():
    return {
            'event_time': datetime.datetime.now().isoformat(),
            'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
            'price': round(random.random() * 100, 2)}

def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
                DeliveryStreamName=stream_name,
                Record={
                    "Data": json.dumps(data)
                    }
                    )

def main(argv):
    stream_name = ''
    region_name = 'us-east-1'

    opts, args = getopt.getopt(argv, "s:r:")
    for opt, arg in opts:
        if opt == '-s':
            stream_name = arg
        elif opt == '-r':
            region_name = arg
    if stream_name == '':
        print("required argument -s <firehose delivery stream name>")
        exit()
    print(f"sending to Kinesis Firehose Deliver Stream {stream_name} in Region {region_name} \n")
    generate(stream_name, boto3.client('firehose', region_name=region_name))

if __name__ == '__main__':
    main(sys.argv[1:])