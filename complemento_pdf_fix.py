from config import config
from daos.invoice_dao import InvoiceDao
from services.aws_service import AwsService
from datetime import datetime
import json
from clients.invoice_manager_client import InvoiceManagerClient

#Configs
config = config()
awsService = AwsService(config)
invoiceDao = InvoiceDao(config)


#Properties
logger = config.property.get('LOGGER')

def main(year=None,month=None,type='Complemento'):
    time = datetime.now()
    path = config.property.get('S3_FACTURA_PATH')
    year = year if year is not None else time.year
    month = month if month is not None else time.month
    logger.info(f'Executing comlpement fix job month:{month} year:{year} type:{type}')
    rows = invoiceDao.get_folios_by_year_and_month_and_type(year,month,type)
    logger.info(f'Type to update rows {len(rows)}')
    for (folio,pre_folio) in rows:
        logger.info(f'folio {folio} and pre_folio {pre_folio}')
        json_file = json.loads(awsService.get_s3_file(config.property.get('S3_BUCKET'),f'{path}{folio}.json'))
        if json_file.get('formaPagoDesc')== 'Por definir' or json_file.get('formaPagoDesc') is None :
            logger.info('updating folio with folio:{} and desc {}'.format(folio,json_file.get('formaPagoDesc')))
            up_dict = {'formaPagoDesc':'Transferencia electrónica de fondos'}
            json_file.update(up_dict)
            json_file = str(json_file).replace("\'", "\"").replace("True", "true").replace("False", "false")
            #logger.info(json_file)
            awsService.update_s3_file(config.property.get('S3_BUCKET'),f'{path}{folio}.json',json_file)
            InvoiceManagerClient.recreate_pdf(folio)
        else:
             logger.info(f'not updating folio:{folio}')
#main()
#main(2022,9)
main(2022,8)