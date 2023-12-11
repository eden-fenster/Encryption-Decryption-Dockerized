# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /encryption_decryption_database_directory


ENV FLASK_APP=database/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY database/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 3000

# Copy database to directory.
COPY database/*.py /encryption_decryption_database_directory/database/


CMD ["flask", "run", "-p", "3000"]