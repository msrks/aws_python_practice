import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('msrks')


with open('test.jpg', 'rb') as f:
    bucket.put_object(Key='test.jpg', Body=f)
