FROM python:3.9

RUN apt update
COPY src/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app/src
ENTRYPOINT ["/app/src/start.sh"]
