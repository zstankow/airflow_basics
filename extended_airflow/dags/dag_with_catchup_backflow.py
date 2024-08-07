from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'zoez',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_catchup_backflow_v3',
    default_args=default_args,
    start_date=datetime(2024, 7, 28),
    schedule_interval='@daily',
    catchup=True
) as dag:
    #here is our task
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo simple bash command!'
    )

    task1