from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'zoez',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
        dag_id='dag_with_taskflow_api',
        default_args=default_args,
        start_date=datetime(2024, 8, 4, 2),
        schedule_interval='@daily'
)

def hello_world():
    
    @task(multiple_outputs=True)
    def get_name():
        return {'first_name': "Jerry3",
                'last_name': "Yolo"}
    
    @task()
    def get_age():
        return 15
    
    @task()
    def greet(first_name, last_name, age):
        print(f'Hello world, my name is {first_name} {last_name}. I am {age} years old')
    
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], 
          last_name=name_dict['last_name'],
          age=age)

hello_world()
