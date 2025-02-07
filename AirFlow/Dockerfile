FROM continuumio/miniconda3

WORKDIR /root/airflow/
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD airflow standalone