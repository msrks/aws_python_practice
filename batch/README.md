https://dev.classmethod.jp/cloud/aws/aws-eaws-ecs-fetch-run-shell/
https://github.com/awslabs/aws-batch-helpers/tree/master/fetch-and-run
https://dev.classmethod.jp/cloud/aws/submit-batch-job-with-api-gateway-and-lambda/

```bash
#1 create docker image 
$ docker build -t awsbatch/fetch_and_run .

#2 create ecr and push docker image
..

#3 upload myjob.sh to s3
$ aws s3 cp myjob.sh s3://<mybucket>/myjob.sh
```


