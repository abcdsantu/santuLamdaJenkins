import json

def lambda_handler(event, context):
    # TODO implement Santu Lamda Jenkins
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Santosh from Lambda!')
    }
