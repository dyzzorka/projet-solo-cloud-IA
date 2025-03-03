from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import requests
import smtplib
from email.message import EmailMessage

# change EMAIL_RECEIVER with ur email
EMAIL_RECEIVER = "dyzzorka@gmail.com"

EMAIL_SENDER = "g2.projet.groupe@gmail.com"
EMAIL_SUBJECT = "Alerte : Erreur API"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "g2.projet.groupe@gmail.com"
SMTP_PASSWORD = "sgkn abnf ntqa ocjz"

def check_api_status():
    url = "https://api-cloud-g2-fb6dd03fa3ff.herokuapp.com/generate"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_email_alert(response.status_code)
    except requests.RequestException as e:
        send_email_alert(str(e))

def send_email_alert(error_message):
    msg = EmailMessage()
    msg.set_content(f"L'API a retourné une erreur : {error_message}")
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

with DAG(
    "api_monitoring_dag",
    start_date=datetime(2025,3,3,19),
    schedule_interval=timedelta(seconds=60),
) as dag:

    check_api = PythonOperator(
        task_id="check_api",
        python_callable=check_api_status
    )

    check_api
