from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import random
from sklearn.datasets import load_iris
import pandas as pd

def load_data(ti):
    data = load_iris()
    df = pd.DataFrame(df.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    return df

def data_db():
    pass

with DAG(
    "training_dag",
    start_date=datetime(2025,1,1),
    schedule_interval=timedelta(seconds=30),
    end_date=datetime(2025,10,10),
    max_active_runs=1,
    max_active_tasks=1
):
    
    task_load_data = PythonOperator(task_id='task_load_data', python_callback=load_data)
    task_data_to_db = PythonOperator(task_id='task_data_to_db', python_callback=data_db)
    
    task_load_data >> task_data_to_db