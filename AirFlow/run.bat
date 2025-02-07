docker build -t airflow-server .

docker run -p 8080:8080 -v "C:\Users\yohan\Desktop\AirFlow:/root/airflow" -it airflow-server