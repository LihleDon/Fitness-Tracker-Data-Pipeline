import boto3
import csv
from io import StringIO
from datetime import datetime
from decimal import Decimal

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

def lambda_handler(event, context):
    # Get the S3 bucket and file details from the event
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]
    
    # Download the CSV from S3
    response = s3_client.get_object(Bucket=bucket, Key=key)
    csv_content = response["Body"].read().decode("utf-8")
    
    # Parse CSV and aggregate by user and date
    csv_reader = csv.DictReader(StringIO(csv_content))
    aggregates = {}
    
    for row in csv_reader:
        user_id = row["user_id"]
        timestamp = datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S")
        date_key = timestamp.strftime("%Y-%m-%d")
        steps = int(row["steps"])
        calories = float(row["calories"])
        
        key = f"{user_id}:{date_key}"
        if key not in aggregates:
            aggregates[key] = {"steps": 0, "calories": 0.0}
        aggregates[key]["steps"] += steps
        aggregates[key]["calories"] += calories
    
    # Store aggregates in DynamoDB
    table = dynamodb.Table("FitnessDailySummaries")
    with table.batch_writer() as batch:
        for key, data in aggregates.items():
            user_id, date = key.split(":")
            batch.put_item(
                Item={
                    "user_id": user_id,
                    "date": date,
                    "total_steps": data["steps"],
                    "total_calories": Decimal(str(round(data["calories"], 2)))
                }
            )
    
    return {
        "statusCode": 200,
        "body": f"Processed {len(aggregates)} daily summaries"
    }