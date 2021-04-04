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
    task_id="date",
    bash_command="date",
    dag=dag,
)

cmd = """
echo 'hello world'
"""

t2 = BashOperator(
    task_id="print",
    bash_command=cmd,
    dag=dag,
)

t1 >> t2
