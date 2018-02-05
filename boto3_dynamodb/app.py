from decimal import Decimal
import random
import datetime
import time
import argparse
import tqdm
import boto3
from boto3.dynamodb.conditions import Key, Attr
#from flask import Flask
#app = Flask(__name__)


TABLE_NAME = 'test_temperature'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)


parser = argparse.ArgumentParser(description="boto3 test")
parser.add_argument('-p', '--put_items', action='store_true', default=False,
                    help='put 100 items to dynamodb')

def put_item():
    ts = Decimal(str(datetime.datetime.now().timestamp()))
    tqdm.tqdm.write(str(ts))
    temp1 = Decimal(str(random.gauss(mu=20, sigma=5)))
    temp2 = Decimal(str(random.gauss(mu=15, sigma=3)))
    table.put_item(
       Item={
            'raspi_id': 1,
            'timestamp': ts,
            'temp': temp1,
        }
    )
    table.put_item(
       Item={
            'raspi_id': 2,
            'timestamp': ts,
            'temp': temp2,
        }
    )

if __name__ == '__main__':
    args = parser.parse_args()

    # put items
    if args.put_items:
        for i in tqdm.tqdm(range(100)):
            put_item()
            time.sleep(.1)

    # get items
    start = Decimal(str(1517496691.22))
    stop = Decimal(str(1517496692.08))
    resp = table.query(
        KeyConditionExpression=Key('raspi_id').eq(1) &
         Key('timestamp').between(start, stop)
    )
    items = resp['Items']
    for i in items:
        print(i)
