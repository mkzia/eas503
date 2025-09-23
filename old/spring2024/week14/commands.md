-  mlflow server --host 127.0.0.1 --port 8080
-  $Env:MLFLOW_TRACKING_URI = "http://127.0.0.1:8080"
-  mlflow models serve -m runs:/cec4153ef4784446b880ea7157f82802/housing_model -p 5000
- mlflow models build-docker -m runs:/cec4153ef4784446b880ea7157f82802/housing_model -n housing_modelv1 --enable-mlserver
- docker login
- docker tag d97b1a436399 mkzia/house_models
- docker push mkzia/house_models
- docker pull mkzia/house_models:latest
- docker run -p 5001:8080 housing_modelv1


$Env:MLFLOW_TRACKING_URI = "https://dagshub.com/mkzia/house_models.mlflow"
mlflow models build-docker --name house_model2 --model-uri "models:/rfr_moodel_n_estimators=150"
