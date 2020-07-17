FROM python:buster
COPY requirements.txt /tmp/requirements.txt
RUN apt update
RUN apt upgrade -y
RUN pip3 install -r /tmp/requirements.txt
