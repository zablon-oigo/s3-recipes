import boto3
from dotenv import load_dotenv
import os
import json

load_dotenv()

region = "us-east-1"
bucket_name = os.getenv("AWS_BUCKET_NAME")
s3_client = boto3.client("s3", region_name=region)

def store_data(bucket_name, key_name, json_data):
    try:
        json_string = json.dumps(json_data)

        s3_client.put_object(Bucket=bucket_name, Key=key_name, Body=json_string)

        return f"JSON data successfully stored in {bucket_name}/{key_name}"

    except Exception as e:
        print(f"Error storing JSON data: {e}")
        return None

sample_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

key_name = "sample_data.json"

result = store_data(bucket_name, key_name, sample_data)
print(result)
