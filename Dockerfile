FROM python:2.7

MAINTAINER Jimmy

COPY source/ /opt/TwitterToRSS/
COPY requirements.txt /opt/TwitterToRSS/

#RUN pip install -r /opt/TwitterToRSS/requirements.txt

ENTRYPOINT exec python /opt/TwitterToRSS/main.py