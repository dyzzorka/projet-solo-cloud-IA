## Projet solo Yohan

<span style="color: red;">**Pour lancer un run ou un push via les fichiers .sh, veuillez être dans le répertoire associé avant de lancer les scripts.**</span>

FastAPI : https://fastapi-yohan-ynov-b4e8901d7995.herokuapp.com/

Streamlit : https://dashboard-yohan-ynov-0ca7039deff6.herokuapp.com/

MLFlow : https://mlflow-yohan-ynov-7591444df070.herokuapp.com/

Pour MLFlow, dans le fichier push.sh, veuillez configurer les variables d'environnement suivantes :

heroku config:set AWS_ACCESS_KEY_ID="<span style="color: red;">**YOUR_AWS_ACCESS_KEY_ID**</span>" --app mlflow-yohan-ynov<br>
heroku config:set AWS_SECRET_ACCESS_KEY="<span style="color: red;">**YOUR_AWS_SECRET_ACCESS_KEY**</span>" --app mlflow-yohan-ynov<br>
heroku config:set BACKEND_STORE_URI="<span style="color: red;">**YOUR_BACKEND_STORE_URI**</span>" --app mlflow-yohan-ynov<br>
heroku config:set ARTIFACT_STORE_URI="<span style="color: red;">**YOUR_ARTIFACT_STORE_URI**</span>" --app mlflow-yohan-ynov<br>
