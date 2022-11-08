import mysql.connector

class InvoiceDao:

    __FACTURAS40_GET_BY_DATE = 'SELECT FOLIO FROM FACTURAS40 WHERE FECHA_ACTUALIZACION BETWEEN \'{}\' AND \'{}\' AND  STATUS_FACTURA IN (3,7) AND TIPO_DOCUMENTO = \'Factura\''
    __REPORTES_DELETE_BY_FOILIO = 'DELETE FROM REPORTES WHERE FOLIO = {}'
    __REPORTES_INSERT = 'INSERT INTO REPORTES(FOLIO,FECHA,TIPO_COMPROBANTE,TOTAL,SUB_TOTAL,FORMA_PAGO,METODO_PAGO,IMP_TRASLADADOS,IMP_RETENIDOS,MONEDA,CANTIDAD,CLAVE_UNIDAD,UNIDAD,CLAVE_PROD_SERV,DESCRIPCION,VALOR_UNITARIO,IMPORTE) VALUES (\'{}\',\'{}\',\'{}\',{},{},\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'
    __FACTURAS40_UPDATE_DATES = 'UPDATE FACTURAS40 SET FECHA_TIMBRADO = \'{}\' , FECHA_CREACION = \'{}\' WHERE FOLIO = \'{}\''

    def __init__(self,config):
        self.config = config
        self.logger = config.property.get('LOGGER')
        self.logger.info('Iniciando conexion de bd')
        dataSource = config.property.get('DATA_SOURCE')
        self.mydb = mysql.connector.connect(
            host=dataSource.get('host'),
            user=dataSource.get('user'),
            password=dataSource.get('password'),
            database=dataSource.get('database'),
            port=dataSource.get('port'))
   
   #Gets facturas from a range period of time
    def getFacturas(self,since,to):
        self.logger.info(self.__FACTURAS40_GET_BY_DATE.format(since,to))
        cursor = self.mydb.cursor()
        cursor.execute(self.__FACTURAS40_GET_BY_DATE.format(since,to))
        return cursor.fetchall()
        
    #Deletes reportes by folio filter    
    def deleteReportesByFolio(self,folio):
        self.logger.info(self.__REPORTES_DELETE_BY_FOILIO.format(folio))
        cursor = self.mydb.cursor()
        cursor.execute(self.__REPORTES_DELETE_BY_FOILIO.format(folio))
        self.logger.info(f'Registers delteted {cursor.rowcount}')
        self.mydb.commit()

    #Updates factura dates by folio   
    def updateFacturas40ByFolio(self,reporte):
        cursor = self.mydb.cursor()
        cursor.execute(self.__FACTURAS40_UPDATE_DATES.format(reporte.get_fecha(),reporte.get_fecha(),reporte.get_folio()))
        self.logger.info(f'Updated registers: {cursor.rowcount}')
        self.mydb.commit()    
    
    #Creates new report data
    def createReporte(self,reporte):
        cursor = self.mydb.cursor()
        cursor.execute(self.__REPORTES_INSERT.format(
            reporte.get_folio(),
            reporte.get_fecha(),
            reporte.get_tipoComprobante(),
            reporte.get_total(),
            reporte.get_subTotal(),
            reporte.get_formaPago(),
            reporte.get_metodoPago(),
            reporte.get_impTrasladados(),
            reporte.get_impRetenidos(),
            reporte.get_moneda(),
            reporte.get_cantidad(),
            reporte.get_claveUnidad(),
            reporte.get_unidad(),
            reporte.get_claveProdServ(),
            reporte.get_descripcion(),
            reporte.get_valorUnitario(),
            reporte.get_importe()))
        self.logger.info(f'Registers inserted {cursor.rowcount}')
        self.mydb.commit()
