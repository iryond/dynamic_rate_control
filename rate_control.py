import boto3
import sys
import json,urllib2

#### for test input
json_text='{"InstanceStates": [{"InstanceId": "i-xxxxxxxx","ReasonCode": "N/A","State": "InService","Description": "N/A"},{"InstanceId": "i-xxxxxxxx","ReasonCode": "N/A","State": "InService","Description": "N/A"}]}'

#### pre
TARGET_STATE = "InService"
ssm = boto3.client('ssm')
ec2 = boto3.client('ec2')

#### main
InstanceStates = json.loads(json_text)
Instances = InstanceStates['InstanceStates']
count = len(Instances)
INSERVICE_NUM = 0

for n in range(0,count):
  InstanceState = Instances[n]['State']
  if InstanceState == TARGET_STATE:
    INSERVICE_NUM = INSERVICE_NUM + 1

print(INSERVICE_NUM)

##### Exex SSM

responce = ec2.describe_instances(
    DryRun=True,
    Filters=[
        {
            'Name': 'tag',
            'Values': [
                'xxxxx*',
            ]
        },
    ],
    NextToken='string',
    MaxResults=123
)

response = ssm.send_command(
    InstanceIds=[
        'string',
    ],
    DocumentName='string',
    DocumentHash='string',
    DocumentHashType='Sha256'|'Sha1',
    TimeoutSeconds=123,
    Comment='string',
    Parameters={
        'string': [
            'string',
        ]
    },
    OutputS3BucketName='string',
    OutputS3KeyPrefix='string',
    ServiceRoleArn='string',
    NotificationConfig={
        'NotificationArn': 'string',
        'NotificationEvents': [
            'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
        ],
        'NotificationType': 'Command'|'Invocation'
    }
)
