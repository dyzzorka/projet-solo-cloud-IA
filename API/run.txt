docker build . -t ynov-api

docker run -p 8000:8000 -e PORT=8000 -v "%cd%:/home/app" -it ynov-api
