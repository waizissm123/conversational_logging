import boto3
import cfg
from botocore.client import Config
from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)

def make_file(data):
    st1=str(data)
    st2=st1+".wav"
    return st2


def aws_upload(local_filename):
    s3 = boto3.client('s3', aws_access_key_id=cfg.aws_access_key,
                      aws_secret_access_key=cfg.aws_secret_key)

    s3.upload_file(local_filename, cfg.aws_bucket, make_file(current_datetime))
    return make_file(current_datetime)


def aws_get_file_url(local_filename):
    s3 = boto3.client('s3', aws_access_key_id=cfg.aws_access_key, aws_secret_access_key= cfg.aws_secret_key,
                     config=Config(signature_version=cfg.signature_version), region_name=cfg.region_name)

    # Generate the URL to get 'key-name' from 'bucket-name'
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': cfg.aws_bucket,
            'Key':  local_filename
        }
    )
    return url

