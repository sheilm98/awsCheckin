import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorLog')

def lambda_handler(event, context):
    # Log the event so you can see it in CloudWatch logs
    print(f"Event: {json.dumps(event)}")
    
    try:
        # Step 1: Extract data correctly regardless of API settings
        if 'body' in event and isinstance(event['body'], str):
            body = json.loads(event['body'])
        else:
            body = event.get('body', event)

        name = body.get('name', 'Still a Stranger')

        # Step 2: Write to DynamoDB
        table.put_item(
            Item={
                'VisitorID': name,
                'Time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )

        # Step 3: Return a perfectly formatted response for the frontend
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': f'Success! Hello {name}'})
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'message': 'Error', 'error': str(e)})}