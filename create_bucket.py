import boto3
from dotenv import load_dotenv
import os

load_dotenv()

region = "us-east-1"
bucket_name = os.getenv("AWS_BUCKET_NAME")
s3_client = boto3.client("s3", region_name=region)

def create_bucket():
    try:
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        print("S3 bucket created successfully")
    
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")
