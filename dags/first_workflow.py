"""
first apache workflow

created on saturday 8th of october 2022

@author: odulaja philip

"""
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from datetime import datetime, timedelta


default_args = {"owner":"airflow", "start_date": datetime(2022, 10, 8)}

with DAG(dag_id='workflow', 
         default_args=default_args,
         schedule_interval='@daily',
        ) as :
