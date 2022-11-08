from config import config
from daos.invoice_dao import InvoiceDao
from services.aws_service import AwsService
from utils import utils
from mappers.factura_mapper import FacturaMapper
from datetime import datetime 

#Configs
config = config()
awsService = AwsService(config)
invoiceDao = InvoiceDao(config)
until = config.property.get('DATASOURCE')

#Properties
logger = config.property.get('LOGGER')

def main(date=None,days=1):
  #Facturas mapped to reports
  correctFolios = []
  incorrectFolios = []

  #Get date filters
  to = datetime.now() if date is None  else date
  since = utils.addDaysToDate(date,days)
  

  #Get facturas to work
  facturas = invoiceDao.get_facturas(since,to)
  logger.info(f'Runing Sync Job with Date{until}')
  for factura in facturas:
    try:
      folio = factura[0]
      logger.info(f'Mapping the factura with folio {folio}')
      path = config.property.get('S3_FACTURA_PATH')
      xml = awsService.get_s3_file(config.property.get('S3_BUCKET'),f'{path}{folio}.xml')
      reports = FacturaMapper.map_xml_to_report(xml)
      invoiceDao.delete_reportes_by_folio(folio)
      logger.info(f'Creating {len(reports)} registers for folio {folio}')
      for report in reports:
        invoiceDao.createReporte(report)
      invoiceDao.update_facturas40_by_folio(report)  
      correctFolios.append(folio) 
    except Exception as e:
      logger.error(e)
      incorrectFolios.append(factura[0])

  logger.info(f'Total Folios:{len(correctFolios)+len(incorrectFolios)}')
  logger.info(f'Correct Folios{correctFolios}')
  logger.info(f'Incorrect Folios{incorrectFolios}')

#date = datetime(2022, 7, 1, 0, 0)
main()
