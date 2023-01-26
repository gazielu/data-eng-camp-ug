#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import time as time
import os
from sqlalchemy import create_engine
import psycopg2
import argparse



# user, passwrd, host, port , database name , table ame

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

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100) #,compression='gzip'


    df = next(df_iter)
    

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name,con=engine,if_exists='append')
    
    while True:

        try:

            start_time = time.time()

            df = next(df_iter)
            # df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            # df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

            df.to_sql(name=table_name, con=engine, if_exists='append')

            end_time = time.time()
            print('its took to iterate %.3f' % (end_time-start_time)) 
    
        except StopIteration:
            print("Finished ingesting data into the ny_taxi")
            break 
    
    
    Number_of_rows = f'''
    select count(*) from zone
    '''
    number_of_rows_in_target = pd.read_sql_query(Number_of_rows, con=engine)
    print(f'numer of rows in target table is {number_of_rows_in_target}')   

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

    

