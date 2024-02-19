# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /encryption_decryption_processor_directory


ENV FLASK_APP=processor/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY processor/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Copy database to directory.
COPY processor/*.py /encryption_decryption_processor_directory/processor/
COPY processor/methods/*.py /encryption_decryption_processor_directory/processor/methods/


CMD ["flask", "run", "-p", "8000"]