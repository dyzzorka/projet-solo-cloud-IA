heroku container:login

heroku create mlflow-yohan-ynov

docker build . -t mlflow-yohan-ynov

docker tag mlflow-yohan-ynov registry.heroku.com/mlflow-yohan-ynov/web

docker push registry.heroku.com/mlflow-yohan-ynov/web

heroku stack:set container -a mlflow-yohan-ynov

heroku config:set AWS_ACCESS_KEY_ID="" --app mlflow-yohan-ynov
heroku config:set AWS_SECRET_ACCESS_KEY="" --app mlflow-yohan-ynov
heroku config:set BACKEND_STORE_URI="" --app mlflow-yohan-ynov
heroku config:set ARTIFACT_STORE_URI="" --app mlflow-yohan-ynov

heroku container:release web -a mlflow-yohan-ynov

heroku open -a mlflow-yohan-ynov 