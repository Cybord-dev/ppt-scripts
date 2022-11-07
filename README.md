# report-sync-job

<!-- ABOUT THE PROJECT -->

## about the project

This job is in charge of align the data from "Facturas40" ddl table in rds of the invoice manager with the table "Reportes"

### Bulded with

Python 3.9

## Construccion del proyecto

```sh
pip install -r requirements.txt
```

### Prerequisites

Python 3.9 or later

### Execution

```sh
python3 ./app.py
```

## Prepare docker image

```sh
docker build -t ppt-platform/report-sync-job:{Version} .
```

## Manual execution

Un comment line 51 from the app class and set the execution date and the days to be processed, then execute the following command:

```sh
python3 app.py
```

<!-- ROADMAP -->

## Roadmap

- [x] 0.0.1 First Phase
- [x] 1.0.0 First stable version
