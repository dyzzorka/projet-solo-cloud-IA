docker build . -t dyzzorka/dashboard

docker run -p 8501:8000 -e PORT=8000 -it dyzzorka/dashboard
