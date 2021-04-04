import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# Initialising the DAG object

dag = DAG(
    dag_id="Reset_DAG",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
)

t1_cmd = """
rm -rf /home/vamsi/Airflow"""

t1 = BashOperator(
    task_id="DeleteFiles",
    bash_command=t1_cmd,
    dag=dag,
)

cmd = """
sudo apt-get update && sudo apt-get install git && sudo apt-get update && sudo apt-get install git && git clone https://github.com/pmvamsi-coder/Airflow.git /home/vamsi/Airflow/
"""

t2 = BashOperator(
    task_id="print",
    bash_command=cmd,
    dag=dag,
)

t1 >> t2
