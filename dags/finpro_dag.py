'''
=================================================
Final Project
FTDS-016-HCK-Group-001

Objective: This program is made to extract data from postgres, transform data until it's analysis ready
Dataset overview: Our data contains information about customer complaints
=================================================
'''

# import libraries
import datetime as dt

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import pandas as pd
from sqlalchemy import create_engine # connection to postgres


# global variables definition
db_name = 'airflow_m3'
username = 'airflow_m3'
password = 'airflow_m3'
host = 'postgres'

# establish connection
postgres_url= f'postgresql+psycopg2://{username}:{password}@{host}/{db_name}'
engine = create_engine(postgres_url)
connection = engine.connect()

# file paths
source_data_path = '/opt/airflow/dags/consumer_complaints_source.csv' # local file that will be sent to postgres
raw_data_path = '/opt/airflow/dags/consumer_complaints_raw.csv'
cleaned_data_path = '/opt/airflow/dags/consumer_complaints_cleaned.csv'

default_args = {
    'owner': 'wilson',
    'start_date': dt.datetime(2024, 6, 20)
    # 'retries': 1,
    # 'retry_delay': dt.timedelta(minutes=5),
}


def csv_to_postgres():
    '''
    this function is made to read a csv file 
    then create a table in the postgres server defined b y arguments received
    '''

    print(connection)
    # load csv from path
    df = pd.read_csv(source_data_path) # local file that will be sent to postgres

    # create a table from df in the connected server
    df.to_sql(name='table_finpro', con=connection, if_exists='replace', index=False)
    print(connection)


def postgres_to_csv():
    '''
    this function is made to pull a table from the postgres server defined by arguments received
    then saving it in csv file format
    '''

    # load table from connected server
    df = pd.read_sql_query('select * from table_finpro', connection)

    # save loaded table into csv format
    df.to_csv(raw_data_path, sep=',', index=False)


def clean_data():
    '''
    this function is made to clean data that's loaded from specified path 
    and saving it in csv file format
    '''
    # load csv from path
    df = pd.read_csv(raw_data_path)

    # turn column names to use snake_case
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('-', '_')
    df.columns = df.columns.str.replace('?', '')

    # drop rows with missing values
    df.dropna(inplace=True)

    # change column order
    df = df[[
        'complaint_id', 'date_received', 'date_sent_to_company',
        'product', 'sub_product', 'issue', 'sub_issue', 
        'consumer_complaint_narrative', 'company_public_response', 
        'company', 'state', 'zip_code', 'tags', 'consumer_consent_provided', 
        'submitted_via', 'company_response_to_consumer', 'timely_response', 'consumer_disputed']]

    # change data type
    df['date_received'] = pd.to_datetime(df['date_received'], format='%m/%d/%Y')
    df['date_sent_to_company'] = pd.to_datetime(df['date_sent_to_company'], format='%m/%d/%Y')

    # save cleaned data to csv format
    df.to_csv(cleaned_data_path, sep=',', index=False)


# dag defintion
with DAG('dag_finpro',
         default_args=default_args,
         description='dag for final project',
         schedule_interval='0 0 * * *', # scheduled to run every 00:00
         catchup=False
         ) as dag:

    # dag's tasks definition
    csv_to_pg_task = PythonOperator(task_id='csv_to_pg',
                             python_callable=csv_to_postgres)
    csv_from_pg_task = PythonOperator(task_id='csv_from_pg',
                             python_callable=postgres_to_csv)
    clean_data_task = PythonOperator(task_id='clean_data',
                             python_callable=clean_data)


# dag's tasks' execution order 
csv_to_pg_task >> csv_from_pg_task >> clean_data_task