import boto3

s3=boto3.resource('s3')

# Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)

# Upload a new file
# data = open('README.md', 'rb')
# s3.Bucket('crystal1').put_object(Key='README.md', Body=data)

import logging
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            print(bucket_name,"~~~~~",region)
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            print(bucket_name,"~~~~~",region)
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
# create_bucket("chalbeee")
# create_bucket("onemorecheapestbucket",region="us-west-2")


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
# upload_file("creatings3bucket.py","crystal1")


s3 = boto3.client('s3')
s3.download_file("crystal1","README.md","READMEee.md")
