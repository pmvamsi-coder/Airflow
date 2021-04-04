from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# Initialising the DAG object

dag = DAG(
    dag_id="test1",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
)

download_launches = BashOperator(
    task_id="print date",
    bash_commands="echo Hellow world",
    dag=dag,
)
