from services.aws_service import AwsService

import logging
import os

class config:
    S3_BUCKET = 'invoice-manager-prod'
    S3_FACTURA_PATH = 'CFDIS/'
    __days = 1
    __properties={}
    __awsConfig = {
        'region_name':'us-west-1'
    }

    def __init__(self):
        logging.basicConfig()
        logger = logging.getLogger('com.ntlink')
        level = getattr(logging, os.getenv('LOG_LEVEL','INFO'))   
        logger.setLevel(level)
        self.__properties['LOGGER'] = logger
        self.__properties['AWS_CONFIG'] = self.__awsConfig
        self.__properties['DAYS'] = self.__days
        self.__properties['S3_BUCKET'] = self.S3_BUCKET
        self.__properties['S3_FACTURA_PATH'] = self.S3_FACTURA_PATH
        ssmRdsSJ = os.getenv('KLIC_CARD_RDS_DATASOURCE','/prod/sj-rds/config')
        service = AwsService(self)
        self.__properties['DATA_SOURCE'] = service.get_ssm_parameter_by_path(ssmRdsSJ)

    @property
    def property(self):
        return self.__properties