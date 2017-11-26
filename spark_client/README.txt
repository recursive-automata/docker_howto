sudo docker build -t jupyter_spark_client .
sudo docker run -it -p 8888:8888 jupyter_spark_client
