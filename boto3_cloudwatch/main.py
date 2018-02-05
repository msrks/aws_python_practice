import random
import datetime
from time import sleep
from decimal import Decimal
from tqdm import tqdm
import boto3


client = boto3.client('cloudwatch')

for i in tqdm(range(100)):
    response = client.put_metric_data(
      Namespace='msrks-ts-test',
      MetricData=[
        {
          'MetricName': 'humidity',
          'Dimensions': [
            {
              'Name': 'Device',
              'Value': 'raspi-1'
            },
          ],
          'Timestamp': datetime.datetime.now().timestamp(),
          'Value': random.random()*30,
          'Unit': 'None'
        },
      ]
    )
    sleep(10)
