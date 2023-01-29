FROM python:3.9.1

RUN pip install --upgrade pip
RUN apt-get install wget
RUN pip install pandas
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY ingest_data_green.py ingest_data_green.py
ENTRYPOINT [ "python", "ingest_data_green.py" ]

