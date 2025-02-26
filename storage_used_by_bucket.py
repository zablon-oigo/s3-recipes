import boto3
from dotenv import load_dotenv
import os

load_dotenv()

region = "us-east-1"
bucket_name = os.getenv("AWS_BUCKET_NAME")
s3_client = boto3.client(
    "s3",
    region_name=region,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

def bucket_storage(bucket_name):
    total_bytes = 0
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        if "Contents" in response:
            # Loop through each object in the bucket and add its size
            for obj in response["Contents"]:
                total_bytes += obj["Size"]
            
            return total_bytes
        else:
            print("Warning: No objects found in the bucket or the bucket does not exist!")
            return 0

    except Exception as e:
        print(f"Error fetching storage details: {e}")
        return 0

storage_used = bucket_storage(bucket_name)
print(f"Total storage used by the bucket: {storage_used} bytes")
