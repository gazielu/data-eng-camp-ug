
import pandas as pd
import time as time
import os
from sqlalchemy import create_engine
import psycopg2
import argparse


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    #os.system(f"wget {url} -O {csv_name}")
    os.system(f"curl -L -o {csv_name} {url}")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000) #,compression='gzip'
    


    # df = next(df_iter)
    
    # df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    # df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    #df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')


# __name__ will work only if we execute it directly 
# argparse = 
# must have 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--user',  help='user name for postgres')
    parser.add_argument('--password',  help='password for postgres')
    parser.add_argument('--host',  help='host for postgres')
    parser.add_argument('--port',  help='port for postgres')
    parser.add_argument('--db',  help='database name for postgres')
    parser.add_argument('--table_name',  help='table where the result stored')
    parser.add_argument('--url',  help='url of the csv file')

    args = parser.parse_args()
    main(args)

    

