import boto3
import json
import io

class AwsService:

    def __init__(self,config):
        self.logger = config.property.get('LOGGER')
        awsConfig = config.property.get('AWS_CONFIG')
        self.s3 = boto3.client(
            service_name='s3',
            region_name=awsConfig.get('region_name'),
        )
        self.ssm = boto3.client(
            service_name='ssm',
            region_name=awsConfig.get('region_name'),
        )
        
    #Gets s3 file by bucket and path
    def get_s3_file(self,bucket,path):
        self.logger.info(f'Getting S3 file in Bucket: {bucket} and path {path}')
        response = self.s3.get_object(Bucket=bucket, Key=path)
        value = response['Body'].read().decode('utf-8')
        return value

    #Gets ssm parameter
    def get_ssm_parameter_by_path(self,parameter):
        self.logger.info(f'Getting ssm parameter: {parameter}')
        response = self.ssm.get_parameter(Name=parameter, WithDecryption=True)
        return json.loads(response['Parameter']['Value'])
    
    #update s3 file by bucket and path
    def update_s3_file(self,bucket,path,content):
        self.logger.info(f'Updating S3 file in Bucket: {bucket} and path {path}')
        self.s3.upload_fileobj(io.BytesIO(str(content).encode("utf-8")),Bucket=bucket, Key=path)