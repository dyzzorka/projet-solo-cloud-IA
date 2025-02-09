heroku container:login

heroku create fastapi-yohan-ynov

docker build . -t fastapi-yohan-ynov

docker tag fastapi-yohan-ynov registry.heroku.com/fastapi-yohan-ynov/web

docker push registry.heroku.com/fastapi-yohan-ynov/web

heroku stack:set container -a fastapi-yohan-ynov

heroku container:release web -a fastapi-yohan-ynov

heroku open -a fastapi-yohan-ynov 