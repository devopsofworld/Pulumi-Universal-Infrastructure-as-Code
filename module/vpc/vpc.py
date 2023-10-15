from pulumi import export
from pulumi_aws import ec2

def create_vpc(vpc_name, cidr_block):
    aws_vpc = ec2.Vpc(vpc_name, 
        cidr_block=cidr_block,
         tags={
            "Name": vpc_name
        }
    )
    export("vpc_id", aws_vpc.id)
    