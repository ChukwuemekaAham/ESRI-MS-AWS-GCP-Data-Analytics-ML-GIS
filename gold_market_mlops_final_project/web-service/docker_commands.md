```shell
#Build the Docker image
docker build -t prediction_model .

#Run the Docker container
docker run -p 8501:8501 prediction_model
```
