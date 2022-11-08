import xml.etree.ElementTree as ET

from models.reporte import Reporte

class FacturaMapper:

    def mapXmlToReport(xml):
        reportes = []
        tree = ET.fromstring(xml)
        totalImpuestosTrasladados = ''
        totalImpuestosRetenidos = ''
        for child in tree:
            if 'Impuestos' in child.tag:
                if 'TotalImpuestosTrasladados' in child.keys():
                    totalImpuestosTrasladados = child.get('TotalImpuestosTrasladados')
                if 'TotalImpuestosRetenidos' in child.keys():
                    totalImpuestosRetenidos = child.get('TotalImpuestosRetenidos')
            if 'Conceptos' in child.tag:
                for concepto in child:
                    if 'Concepto' in concepto.tag:
                        reporte = Reporte()
                        reporte.set_fecha(tree.get('Fecha'))
                        reporte.set_folio(tree.get('Folio'))
                        reporte.set_tipoComprobante(tree.get('TipoDeComprobante'))
                        reporte.set_total(tree.get('Total'))
                        reporte.set_moneda(tree.get('Moneda'))
                        reporte.set_subTotal(tree.get('SubTotal'))
                        reporte.set_metodoPago(tree.get('MetodoPago'))
                        reporte.set_formaPago(tree.get('FormaPago'))
                        reporte.set_cantidad(concepto.get('Cantidad'))
                        reporte.set_claveUnidad(concepto.get('ClaveUnidad'))
                        reporte.set_unidad(concepto.get('Unidad'))
                        reporte.set_claveProdServ(concepto.get('ClaveProdServ'))
                        reporte.set_descripcion(concepto.get('Descripcion').replace("'", ""))
                        reporte.set_valorUnitario(concepto.get('ValorUnitario'))
                        reporte.set_importe('')
                        for conceptoChild in concepto:
                            if 'Impuestos' in conceptoChild.tag:
                                for traslados in conceptoChild:
                                    if 'Traslados' in traslados.tag:
                                        for traslado in traslados:
                                            if 'Traslado' in traslado.tag:
                                                reporte.set_importe(traslado.get('Importe'))

                        reportes.append(reporte)
        for reporte in reportes:
            reporte.set_impTrasladados(totalImpuestosTrasladados)
            reporte.set_impRetenidos(totalImpuestosRetenidos)

        return reportes