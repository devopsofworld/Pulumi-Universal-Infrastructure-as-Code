import pulumi
from module.s3.s3_bucket import create_s3_bucket
from config import bucket_name  # Import the variable from config.py
from config import vpc_name,cidr_block
from module.vpc.vpc import create_vpc

# Call the create_s3_bucket function with the bucket_name
create_s3_bucket(bucket_name)
create_vpc(vpc_name,cidr_block)

