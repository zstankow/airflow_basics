from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'zoez',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_sklearn():
    import sklearn
    print(f"scikit-learn with version: {sklearn.__version__}")

def get_matplotlib():
    import matplotlib
    print(f"matplotlib with version: {matplotlib.__version__}")

with DAG(
    dag_id='dag_with_python_dependencies',
    default_args=default_args,
    description='This is our first dag',
    start_date=datetime(2024, 8, 4),
    schedule_interval='@daily',
    catchup=True
) as dag:
    
    get_sklearn = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )

    get_matplotlib = PythonOperator(
        task_id='get_matplotlib',
        python_callable=get_matplotlib
    )

    get_sklearn >> get_matplotlib