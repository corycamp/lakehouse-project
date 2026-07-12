import boto3
from botocore.client import Config

s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id = 'minioadmin',
    aws_secret_access_key = 'minioadmin',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

s3.upload_file('sample.txt', 'raw', 'sample.txt')

print("File uploaded successfully!")