# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /encryption_decryption_database_directory

ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0


COPY database/requirements.txt requirements.txt
RUN apt-get -y update
RUN apt-get install inetutils-ping
RUN apt-get -y install curl
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 3000

WORKDIR ../app
# Copy database to directory.
COPY database/app.py /encryption_decryption_database_directory/app/app.py
COPY database/log_database.py /encryption_decryption_database_directory/app/log_database.py
COPY database/database_storage.py /encryption_decryption_database_directory/app/database_storage.py


WORKDIR ../database
COPY database/create_database.py /encryption_decryption_database_directory/database/create_database.py

WORKDIR /encryption_decryption_database_directory

CMD ["flask", "run", "-p", "3000"]