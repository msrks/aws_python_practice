import os
from datetime import datetime
from io import BytesIO
# from PIL import Image
import boto3
from flask import Flask, request, render_template, redirect, url_for

BUCKET = "xxxxx"
# check JOB_QUEUE by typing `$ aws batch describe-job-queues`
JOB_QUEUE = "arn:aws:batch:ap-northeast-1:xxxxxxxxxxxx:job-queue/test-job-queues"
JOB_DEFINITION = "test-job-def:1"

app = Flask(__name__)
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
# UPLOAD_FOLDER = './uploads'
# app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/img', methods=['POST'])
def img():
    image = request.files["img"]
    #image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    #image = Image.open(BytesIO(image))

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET)
    bucket.put_object(Key=image.filename, Body=image.read(), ACL='public-read')

    client = boto3.client('s3')
    waiter = client.get_waiter('object_exists').wait(Bucket=BUCKET, Key=image.filename)

    client = boto3.client('batch')
    response = client.submit_job(
        jobName = 'job-' + datetime.now().strftime('%Y%m%d-%H%M%S'),
        jobQueue = JOB_QUEUE,
        jobDefinition = JOB_DEFINITION
        )

    return redirect(url_for('index'))
