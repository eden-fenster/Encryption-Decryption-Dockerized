# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /encryption_decryption_web_directory


ENV FLASK_APP=web/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY web/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

# Copy database to directory.
COPY web/*.py /encryption_decryption_web_directory/web/
COPY web/templates/*.html /encryption_decryption_web_directory/web/templates/
COPY web/static/styles/*.css /encryption_decryption_web_directory/web/static/styles/


CMD ["flask", "run"]