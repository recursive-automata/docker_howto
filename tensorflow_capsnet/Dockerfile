FROM gcr.io/tensorflow/tensorflow:latest-gpu

COPY entrypoint.sh     /home/
COPY download_mnist.py /home/
COPY unzip_data.sh     /home/

WORKDIR /home
CMD bash entrypoint.sh
