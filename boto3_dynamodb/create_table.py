import boto3

TABLE_NAME = 'test_temperature'

WARN = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

dynamodb = boto3.resource('dynamodb')

try:
    table = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': 'raspi_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'timestamp',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'raspi_id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'timestamp',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    table.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME)

except Exception as e:
    print (FAIL+str(e)+ENDC)

# Print out some data about the table.
creted_at = dynamodb.Table(TABLE_NAME).creation_date_time
print(f"{TABLE_NAME} created at {creted_at}")
