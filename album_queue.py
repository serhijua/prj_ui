import boto3
import json

sqs = boto3.resource('sqs')
albums = sqs.get_queue_by_name(QueueName='test123')

def request_album(data):
  dataAsString = json.dumps(data)
  response = albums.send_message(MessageBody=dataAsString)
