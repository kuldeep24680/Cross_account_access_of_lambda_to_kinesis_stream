import boto3
import json
from datetime import datetime
import calendar
import random
import time


# creating client for sts connection
client = boto3.client('sts')

# specifications of rolearn and connection duration required for assume role
sts_response = client.assume_role(RoleArn="arn:aws:iam::003644705123:role/onepurchase-uki-bookings-kinesis",                              
                                      RoleSessionName='AssumePocRole', DurationSeconds=900)

# Name of the stream									  
my_stream_name = 'test_stream'

# details for connection like region, credentials and session_token
kinesis_client = boto3.client('kinesis', region_name='eu-central-1',aws_access_key_id = sts_response['Credentials']['AccessKeyId'],
                              aws_secret_access_key = sts_response['Credentials']['SecretAccessKey'],
                              aws_session_token = sts_response['Credentials']['SessionToken'])

							  
# handler function for ingesting into the stream in caspian account
def lambda_handler(event, context):
    property_value = str(random.randint(40, 120))
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    metadata = {'usecase': 'Analytics', 'source': 'testing','business': 'Streaming', 'retention': random.randint(5, 150),
                'quality': 'High','confidentiality': 'High','expiration': random.randint(5, 50), 'refresh_velocity': random.randint(5, 150),'url': 'test/file'+str(random.randint(1, 1500))}


    data =  "This is a sample data, which is not to be touched or altered. Sample with ID: 60"
    payload = {
                "prop": str(property_value),
                "timestamp": str(property_timestamp),
                "data": data,
                "metadata": metadata
              }
              
    print(payload)
    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey='123')
    print("data has been ingested to respective kinesis stream")
    
    

