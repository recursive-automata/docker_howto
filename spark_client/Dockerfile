FROM ubuntu

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	python3 \
	python3-pip \
	default-jdk

RUN export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN pip3 install --upgrade pip
RUN pip3 install setuptools
RUN pip3 install jupyter
RUN pip3 install pyspark numpy scipy pandas matplotlib

RUN ln -s /usr/bin/python3 /usr/bin/python

EXPOSE 8888
WORKDIR /home

COPY connection_count.py    /home/
COPY connection_count.ipynb /home/

CMD jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root 
