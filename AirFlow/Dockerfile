FROM continuumio/miniconda3

WORKDIR /root/airflow

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY dags/ dags/

RUN if test -d plugins/ ; then \
    COPY plugins/ plugins/ ; \
  fi

RUN if test -f train.py ; then \
    COPY train.py . ; \
  fi

RUN if test -f airflow.db ; then \
    COPY airflow.db . ; \
  fi

CMD airflow standalone