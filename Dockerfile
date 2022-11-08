FROM python:3

WORKDIR /app
ADD ./ /app/

COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt

#CMD [ "python", "/app/report_sync.py" ]
CMD [ "python", "/app/pre_folio_fix.py" ]