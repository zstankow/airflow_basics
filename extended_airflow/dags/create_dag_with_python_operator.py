from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

def greet(**kwargs):
    ti = kwargs['ti']
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f'Hello world! My name is {first_name} {last_name} and i am {age} years old')

def get_name(**kwargs):
    ti = kwargs['ti']
    ti.xcom_push(key='first_name', value='Jerry2')
    ti.xcom_push(key='last_name', value='Fridman2')

def get_age(**kwargs):
    ti = kwargs['ti']
    ti.xcom_push(key='age', value='20')

default_args = {
    'owner': 'zoez',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}
with DAG(
    dag_id='with_python_operator',
    default_args=default_args,
    description='This is our first dag with python operator',
    start_date=datetime(2024, 8, 4, 2),
    schedule_interval='@daily'
) as dag:
    #here is our task
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
        # op_kwargs={'age': 11}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
