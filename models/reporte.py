class Reporte():

    def __init__(self):
        pass

    def get_folio(self):
        return self.__folio

    def set_folio(self,folio):
        self.__folio=folio

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self,fecha):
        self.__fecha=fecha

    def get_tipoComprobante(self):
        return self.__tipoComprobante

    def set_tipoComprobante(self,tipoComprobante):
        self.__tipoComprobante=tipoComprobante

    def get_total(self):
        return self.__total

    def set_total(self,total):
        self.__total=total

    def get_subTotal(self):
        return self.__subTotal

    def set_subTotal(self,subTotal):
        self.__subTotal=subTotal

    def get_impTrasladados(self):
        return self.__impTrasladados

    def set_impTrasladados(self,impTrasladados):
        self.__impTrasladados=impTrasladados

    def get_impRetenidos(self):
        return self.__impRetenidos

    def set_impRetenidos(self,impRetenidos):
        self.__impRetenidos=impRetenidos

    def get_metodoPago(self):
        return self.__metodoPago

    def set_metodoPago(self,metodoPago):
        self.__metodoPago=metodoPago

    def get_formaPago(self):
        return self.__formaPago

    def set_formaPago(self,formaPago):
        self.__formaPago=formaPago

    def get_moneda(self):
        return self.__moneda

    def set_moneda(self,moneda):
        self.__moneda=moneda

    #Concepto objects
    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self,cantidad):
        self.__cantidad=cantidad

    def get_claveUnidad(self):
        return self.__claveUnidad

    def set_claveUnidad(self,claveUnidad):
        self.__claveUnidad=claveUnidad

    def get_unidad(self):
        return self.__unidad

    def set_unidad(self,unidad):
        self.__unidad=unidad

    def get_claveProdServ(self):
        return self.__claveProdServ

    def set_claveProdServ(self,claveProdServ):
        self.__claveProdServ=claveProdServ

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self,descripcion):
        self.__descripcion=descripcion

    def get_valorUnitario(self):
        return self.__valorUnitario

    def set_valorUnitario(self,valorUnitario):
        self.__valorUnitario=valorUnitario

    def get_importe(self):
        return self.__importe

    def set_importe(self,importe):
        self.__importe=importe