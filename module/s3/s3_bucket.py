from pulumi import export
from pulumi_aws import s3

def create_s3_bucket(bucket_name):
    # Create an AWS resource (S3 Bucket) using the provided bucket_name
    bucket = s3.Bucket(bucket_name)
    export('bucket_name', bucket.id)
