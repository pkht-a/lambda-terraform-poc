import json
import requests
import boto3

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda loaded from a different GitHub! Edit No. 2.')
    }
