from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'zoez',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}
with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is our first dag',
    start_date=datetime(2024, 8, 4, 2),
    schedule_interval='@daily'
) as dag:
    #here is our task
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task!'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo im task 2, running after task 1!'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo im task 3, running after task 1, at the same time as task2!'
    )

# Method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

# Method 2
    # task1 >> task2
    # task1 >> task3

# Method 3
    task1 >> [task2, task3]