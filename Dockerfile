# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /political_insults_processor_directory


ENV FLASK_APP=processor/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY processor/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Copy database to directory.
COPY processor/*.py /political_insults_processor_directory/processor/


CMD ["flask", "run", "-p", "8000"]