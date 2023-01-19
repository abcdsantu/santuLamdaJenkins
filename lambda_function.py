import json

def lambda_handler(event, context):
    # TODO implement Santu Lamda Jenkins and create release v1.0
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Santosh from Lambda!:v1.0')
    }
