#!/usr/bin/env python3
"""Encryption Decryption - Query Database"""
import datetime
import logging

import requests
from flask import Flask, render_template, render_template_string, request

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

DATABASE_SERVER: str = "encryption_decryption_database"
DATABASE_PORT: str = "3000"

# pylint: disable = logging-fstring-interpolation

app = Flask(__name__)


# return the database.
@app.route('/')
def home():
    """Get dates"""
    logging.debug("Displaying dates page")
    return render_template('dates.html')


# Putting a template for when the dates will be received.
@app.route('/queried', methods=['GET', 'POST'])
def return_queried():
    """Return queried"""
    # Getting dates.
    start_date = request.form.get('startdate')
    end_date = request.form.get('enddate')
    if not isinstance(start_date, str):
        raise ValueError(f"{start_date} is of invalid type {type(start_date)}")
    if not isinstance(end_date, str):
        raise ValueError(f"{end_date} is of invalid type {type(end_date)}")
    logging.debug\
        ("Received dates\nThe start date is %s and the end date is %s", start_date, end_date)
    # Send to database.
    dates_to_send: dict = {"Start": start_date, "End": end_date}
    requests.post\
        (f'http://{DATABASE_SERVER}:{DATABASE_PORT}/queried', json=dates_to_send, timeout=10)
    logging.debug(f"Sent dates {dates_to_send} to be queried")
    response = requests.get(f'http://{DATABASE_SERVER}:{DATABASE_PORT}/queried', timeout=10)
    if not response:
        raise SystemError('Unable to get queried dates')
    logging.debug("Received queried dates back")
    return render_template('results.html', Title='Queried Database',
                           Second='Database Results') \
        + render_template_string(response.json())


@app.route('/database')
def return_all():
    """Return all"""
    response = requests.get(f'http://{DATABASE_SERVER}:{DATABASE_PORT}/database', timeout=10)
    if not response:
        raise SystemError('Unable to get dates')
    logging.debug("Returning all dates")
    return render_template\
        ('results.html', Title='Full Database') + render_template_string(response.json())


if __name__ == '__main__':
    app.run(debug=True, port=1000, host='encryption_decryption_query')
