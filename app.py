from config import config
from invoice_dao import InvoiceDao
from aws_service import AwsService
from utils import utils
from factura_mapper import FacturaMapper
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
  facturas = invoiceDao.getFacturas(since,to)
  logger.info(f'Runing Sync Job with Date{until}')
  for factura in facturas:
    try:
      folio = factura[0]
      logger.info(f'Mapping the factura with folio {folio}')
      path = config.property.get('S3_FACTURA_PATH')
      xml = awsService.getS3File(config.property.get('S3_BUCKET'),f'{path}{folio}.xml')
      reports = FacturaMapper.mapXmlToReport(xml)
      invoiceDao.deleteReportesByFolio(folio)
      logger.info(f'Creating {len(reports)} registers for folio {folio}')
      for report in reports:
        invoiceDao.createReporte(report)
      invoiceDao.updateFacturas40ByFolio(report)  
      correctFolios.append(folio) 
    except Exception as e:
      logger.error(e)
      incorrectFolios.append(factura[0])

  logger.info(f'Total Folios:{len(correctFolios)+len(incorrectFolios)}')
  logger.info(f'Correct Folios{correctFolios}')
  logger.info(f'Incorrect Folios{incorrectFolios}')

#date = datetime(2022, 1, 1, 0, 0)
main()