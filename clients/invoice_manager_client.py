import requests

class InvoiceManagerClient:


    #recreate pdf
    def recreate_pdf(folio):
       
       url = 'http://localhost:8080/api/facturas/{}/reconstruccion-pdf'.format(folio) 
       x = requests.post(url, folio)
       print(f'The folio {folio} had status {x.status_code}')