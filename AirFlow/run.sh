#!/bin/bash

docker build -t airflow-server .

docker run -p 8081:8080 -v "C:\Users\yohan\OneDrive\Bureau\IA-dans le cloud\projet-solo-cloud-IA\AirFlow:/root/airflow" -it airflow-server
