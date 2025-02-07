from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import random

def random_number(ti):
    ti.xcom_push(key='MY_KEY', value='KEY_API')
    return random.randint(1, 1000)

def print_hello(ti, name='yohan'):
    nb = ti.xcom_pull(task_ids="first_task", key='return_value')
    key = ti.xcom_pull(task_ids="first_task", key='MY_KEY')
    print(f"Hello {name}", nb)
    return nb
    
def random_task():
    return random.choice(["task_1", "task_2"])

def print_goodbye():
    print("Goodbye")

with DAG(
    "my_first_dag",
    start_date=datetime(2025,1,1),
    schedule_interval=timedelta(seconds=30),
    end_date=datetime(2025,10,10),
    max_active_runs=1,
    max_active_tasks=1
):
    task_random_choice = BranchPythonOperator (task_id="task_random_choice", python_callable=random_task)
    
    first_task = PythonOperator(
        task_id="first_task",
        python_callable=random_number
    )
    
    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=print_hello,
        op_kwargs={'name': 'bob'}
    )
    task_2 = PythonOperator(
        task_id="task_2",
        python_callable=print_hello,
        op_kwargs={'name': 'bob'}
    )
    
    task_goodbye = PythonOperator(
        task_id="task_goodbye",
        python_callable=print_goodbye
    )
    
    task_bash = BashOperator(
        task_id="task_bash",
        bash_command="echo 'Hello world' >> /root/airflow/test.txt"
    )
    
    first_task >> task_bash >> task_random_choice >> [task_1, task_2] >> task_goodbye