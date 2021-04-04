import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# Initialising the DAG object

dag = DAG(
    dag_id="test1",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
)

t1 = BashOperator(
    task_id="print date",
    bash_commands="echo Hellow world",
    dag=dag,
)

t2 = BashOperator(
    task_id="print date",
    bash_commands="echo Hellow world",
    dag=dag,
)

t1 >> t2
