import boto3
import sys
import json,urllib2

#### for test input
json_text='{"InstanceStates": [{"InstanceId": "i-1add5d1f","ReasonCode": "N/A","State": "InService","Description": "N/A"},{"InstanceId": "i-b9bb39be","ReasonCode": "N/A","State": "InService","Description": "N/A"}]}'

#print (root)
#print (root['InstanceStates'])

#### pre
TARGET_STATE = "InService"

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

