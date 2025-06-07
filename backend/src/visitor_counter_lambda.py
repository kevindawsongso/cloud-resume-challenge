# Place this file in: src/visitor_counter_lambda.py

import boto3
import os
import json

# Get the table name from an environment variable set by the SAM template
TABLE_NAME = os.environ.get('DYNAMODB_TABLE_NAME', 'visitor-counter')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

COUNTER_ITEM_ID = 'myResumePageCounter'
COUNT_ATTRIBUTE_NAME = 'visit_count'

def lambda_handler(event, context):
    try:
        # Get the current item
        response = table.get_item(
            Key={
                'ItemID': COUNTER_ITEM_ID
            }
        )

        if 'Item' in response:
            # IMPORTANT: Convert the Decimal type from DynamoDB to a standard Python int
            current_count = int(response['Item'].get(COUNT_ATTRIBUTE_NAME, 0))
        else:
            current_count = 0

        new_count = current_count + 1

        # Update the item in DynamoDB with the new count
        table.update_item(
            Key={
                'ItemID': COUNTER_ITEM_ID
            },
            UpdateExpression=f'SET {COUNT_ATTRIBUTE_NAME} = :val',
            ExpressionAttributeValues={
                ':val': new_count
            }
        )

        # Return the new count, ensuring it's a standard integer for JSON serialization
        return {
            'statusCode': 200,
            # CORS headers are now handled by API Gateway as defined in template.yaml,
            # but it's good practice to keep them here as a fallback or for local testing.
            'headers': {
                "Access-Control-Allow-Origin": "*", # Replace with your domain in production
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, OPTIONS"
            },
            'body': json.dumps({'count': new_count})
        }

    except Exception as e:
        print(f"Error: {e}")
        # Return a server error response
        return {
            'statusCode': 500,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, OPTIONS"
            },
            'body': json.dumps({'error': str(e)})
        }
