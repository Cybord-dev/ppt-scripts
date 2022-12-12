from config import config
from daos.invoice_dao import InvoiceDao
from services.aws_service import AwsService
from datetime import datetime

#Configs
config = config()
awsService = AwsService(config)
invoiceDao = InvoiceDao(config)

#Properties
logger = config.property.get('LOGGER')

def main(year=None,month=None):
    time = datetime.now()
    path = config.property.get('S3_FACTURA_PATH')
    year = year if year is not None else time.year
    month = month if month is not None else time.month
    logger.info(f'Executing pre folio fix job month:{month} year:{year}')
    duplicated_rows = invoiceDao.get_duplicated_pre_folios_by_year_and_month(year,month)
    logger.info(f'Duplicated rows {duplicated_rows}')
    if duplicated_rows > 0:
       folios = invoiceDao.get_folios_by_year_and_month(year,month)
       logger.info(f'Facturas in the month {len(folios)}')
       counter = 0
       for (folio,prefolio) in folios:
            counter += 1
            new_pre_folio = f'{str(month).zfill(2)}{str(year)[2:]}-{str(counter).zfill(5)}'
            logger.info(f'folio:{folio} pre_folio:{new_pre_folio}')
            json_file = str(awsService.get_s3_file(config.property.get('S3_BUCKET'),f'{path}{folio}.json'))
            json_file = json_file.replace(prefolio, new_pre_folio)
            invoiceDao.update_factura_prefolio_by_folio(folio,new_pre_folio)
            awsService.update_s3_file(config.property.get('S3_BUCKET'),f'{path}{folio}.json',json_file)
            

#main(2022,11)
main()