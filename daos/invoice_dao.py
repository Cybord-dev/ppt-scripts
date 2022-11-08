import mysql.connector

class InvoiceDao:

    __FACTURAS40_GET_BY_DATE = 'SELECT FOLIO FROM FACTURAS40 WHERE FECHA_ACTUALIZACION BETWEEN \'{}\' AND \'{}\' AND  STATUS_FACTURA IN (3,7) AND TIPO_DOCUMENTO = \'Factura\''
    __REPORTES_DELETE_BY_FOILIO = 'DELETE FROM REPORTES WHERE FOLIO = {}'
    __REPORTES_INSERT = 'INSERT INTO REPORTES(FOLIO,FECHA,TIPO_COMPROBANTE,TOTAL,SUB_TOTAL,FORMA_PAGO,METODO_PAGO,IMP_TRASLADADOS,IMP_RETENIDOS,MONEDA,CANTIDAD,CLAVE_UNIDAD,UNIDAD,CLAVE_PROD_SERV,DESCRIPCION,VALOR_UNITARIO,IMPORTE) VALUES (\'{}\',\'{}\',\'{}\',{},{},\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'
    __FACTURAS40_UPDATE_DATES = 'UPDATE FACTURAS40 SET FECHA_TIMBRADO = \'{}\' , FECHA_CREACION = \'{}\' WHERE FOLIO = \'{}\''
    __FACTURAS40_WITH_DUPLICATED_FOLIO = 'SELECT COUNT(1) '\
                                         'FROM ( '\
                                            'SELECT PRE_FOLIO,count(1) '\
                                            'FROM FACTURAS40  '\
                                            'WHERE YEAR(fecha_creacion) = {} '\
                                                'AND MONTH(fecha_creacion) = {}  '\
                                                'group by PRE_FOLIO '\
                                           'having count(1)>1) t1 '
    __FACTURAS40_BY_YEAR_AND_MONTH = 'SELECT FOLIO,PRE_FOLIO '\
                                     'FROM FACTURAS40 '\
                                     'WHERE MONTH(fecha_creacion) = MONTH(CURRENT_DATE()) '\
                                        'AND YEAR(fecha_creacion) = YEAR(CURRENT_DATE())'
                                
    __FACTURAS40_UPDATE_PREFOLIO_BY_DATE = 'UPDATE FACTURAS40 SET PRE_FOLIO = \'{}\'  WHERE FOLIO = \'{}\''

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
    def get_facturas(self,since,to):
        self.logger.info(self.__FACTURAS40_GET_BY_DATE.format(since,to))
        cursor = self.mydb.cursor()
        cursor.execute(self.__FACTURAS40_GET_BY_DATE.format(since,to))
        return cursor.fetchall()
        
    #Deletes reportes by folio filter    
    def delete_reportes_by_folio(self,folio):
        self.logger.info(self.__REPORTES_DELETE_BY_FOILIO.format(folio))
        cursor = self.mydb.cursor()
        cursor.execute(self.__REPORTES_DELETE_BY_FOILIO.format(folio))
        self.logger.info(f'Registers delteted {cursor.rowcount}')
        self.mydb.commit()

    #Updates factura dates by folio   
    def update_facturas40_by_folio(self,reporte):
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

    #Get amount  of duplicated pre folios by year and month
    def get_duplicated_pre_folios_by_year_and_month(self,year,month):
        self.logger.info(self.__FACTURAS40_WITH_DUPLICATED_FOLIO.format(year,month))
        cursor = self.mydb.cursor()
        cursor.execute(self.__FACTURAS40_WITH_DUPLICATED_FOLIO.format(year,month))
        duplicatedPreFolios = 0
        records = cursor.fetchall()
        for element in records:
            duplicatedPreFolios = element[0]
        return duplicatedPreFolios
    
    #Get folios by year and month
    def get_folios_by_year_and_month(self,year,month):
        self.logger.info(self.__FACTURAS40_BY_YEAR_AND_MONTH.format(year,month))
        cursor = self.mydb.cursor()
        cursor.execute(self.__FACTURAS40_BY_YEAR_AND_MONTH.format(year,month))
        return cursor.fetchall()

    def update_factura_prefolio_by_folio(self,folio,prefolio):
        cursor = self.mydb.cursor()
        cursor.execute(self.__FACTURAS40_UPDATE_PREFOLIO_BY_DATE.format(prefolio,folio))
        self.logger.info(f'Updated registers: {cursor.rowcount}')
        self.mydb.commit()   