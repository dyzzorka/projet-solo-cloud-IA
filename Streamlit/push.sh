heroku container:login

heroku create dashboard-yohan-ynov

docker build . -t dashboard-yohan-ynov

docker tag dashboard-yohan-ynov registry.heroku.com/dashboard-yohan-ynov/web

docker push registry.heroku.com/dashboard-yohan-ynov/web

heroku stack:set container -a dashboard-yohan-ynov

heroku container:release web -a dashboard-yohan-ynov

heroku open -a dashboard-yohan-ynov