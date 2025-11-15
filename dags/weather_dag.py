from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta
import sys



sys.path.insert(0, "/opt/airflow")
from Weather_Storyteller.weather_report import generate_weather_report


# générer le rapport météo
def weather_report_to_html(report):
    """
    Transforme le dictionnaire weather_report en contenu HTML optimisé pour email.
    """
    html_content = f"""
    <html>
    <body style="font-family:Arial,sans-serif; line-height:1.5; color:#333;">
        <h2>🌤 Bulletin météo IA - {report['city']}</h2>

        <h3>📊 Informations principales</h3>
        <ul>
            <li><strong>Température:</strong> {report['temp']}°C (Ressenti: {report['feels_like']}°C)</li>
            <li><strong>Temp min/max:</strong> {report['temp_min']}°C / {report['temp_max']}°C</li>
            <li><strong>Humidité:</strong> {report['humidity']}%</li>
            <li><strong>Vent:</strong> {report['wind_speed']} m/s</li>
            <li><strong>Description:</strong> {report['description']}</li>
            <li><strong>Pression:</strong> {report['pressure']} hPa</li>
            <li><strong>Nuages:</strong> {report['clouds']}%</li>
            <li><strong>Lever du soleil:</strong> {report['sunrise']} | <strong>Coucher:</strong> {report['sunset']}</li>
        </ul>

        <h3>📝 Rapport IA</h3>
        <p>{report.get('narrative', 'Narrative non disponible.')}</p>

        <hr>
        <p style="font-size:0.9em; color:#666;">Bulletin généré automatiquement par Weather Storyteller</p>
    </body>
    </html>
    """
    return html_content

def run_weather_report(ti):
    report = generate_weather_report("Casablanca")
    html_content = weather_report_to_html(report)
    ti.xcom_push(key='weather_html', value=html_content)



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
    schedule='0 7 * * *',
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
    html_content="{{ ti.xcom_pull(task_ids='run_weather_report', key='weather_html') }}",
    conn_id='smtp_default',
    dag=dag,
)




run_weather_task >> send_email_task
