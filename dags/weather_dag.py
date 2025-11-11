from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta
import sys
import os

# Ajouter le chemin de Weather_Storyteller
sys.path.insert(0, "/opt/airflow")
from Weather_Storyteller.weather_report import generate_weather_report


# Tâche pour générer le rapport météo
def run_weather_report(ti):
    report = generate_weather_report("Casablanca")
    # print("=== Generated Weather Report ===")
    print(report)
    # Push dans XCom pour récupérer dans l'email
    ti.xcom_push(key='weather_report', value=report)

# Arguments par défaut du DAG
default_args = {
    'owner': 'Ibtissam',
    'depends_on_past': False,
    'start_date': datetime(2025, 11, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_dag',
    default_args=default_args,
    description='DAG pour générer et envoyer un bulletin météo IA',
    schedule=timedelta(minutes=2),  # TEST : toutes les 5 minutes
    catchup=False,
)

# Tâche génération météo
run_weather_task = PythonOperator(
    task_id='run_weather_report',
    python_callable=run_weather_report,
    dag=dag,
)

# Tâche envoi par email
send_email_task = EmailOperator(
    task_id='send_weather_email',
    to='ibtissamerrachidi81@gmail.com',
    subject='Bulletin météo Casablanca',
    html_content="{{ ti.xcom_pull(task_ids='run_weather_report', key='weather_report') }}",
    conn_id='smtp_default',
    dag=dag,
)

# Dépendance
run_weather_task >> send_email_task
