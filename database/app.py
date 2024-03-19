#!/usr/bin/env python3
"""Encryption Decryption - Database"""
import json
import logging
import re

from datetime import datetime
from database_storage import Storage

from flask import Flask, request

DATABASE_DIRECTORY: str = 'database'
DATABASE_NAME: str = 'encryption_decryption_results'

app = Flask(__name__)

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# pylint: disable=invalid-name

# A class with all of our things
encryption_decryption: Storage = Storage(directory=DATABASE_DIRECTORY, database_name=DATABASE_NAME)


# Returns the results
@app.route('/database')
def get_database():
    """Getting from database"""
    return json.dumps(encryption_decryption.database.show_all())


@app.route('/database', methods=['POST'])
def add_to_database():
    """Adding to database"""
    # Adding to list.
    encryption_decryption.responses.append(request.get_json())
    original = encryption_decryption.responses[len(encryption_decryption.responses) - 1]["Original"]
    translated = encryption_decryption.responses[len(encryption_decryption.responses) - 1]["Translated"]
    encordec = encryption_decryption.responses[len(encryption_decryption.responses) - 1]["Encrypt or Decrypt ?"]
    time = encryption_decryption.responses[len(encryption_decryption.responses) - 1]["Time"]
    date = datetime.strptime(encryption_decryption.responses[len(encryption_decryption.responses) - 1]["Date"], '%Y-%m-%d %H:%M')
    # If of wrong type, raise value error.
    if not isinstance(original, str):
        raise ValueError(f"Variable {original} is of wrong type {type(original)}")
    if not isinstance(translated, str):
        raise ValueError(f"Variable {translated} is of wrong type {type(translated)}")
    if not isinstance(encordec, str):
        raise ValueError(f"Variable {encordec} is of wrong type {type(encordec)}")
    if not isinstance(time, str):
        raise ValueError(f"Variable {time} is of wrong type {type(time)}")
    if not isinstance(date, datetime):
        raise ValueError(f"Variable {date} is of wrong type {type(date)}")
    # Adding to database
    logging.debug("Original -> %s \n Translated -> %s \n Encrypt or Decrypt ? -> %s \n Time -> %s \n Date -> %s", original, translated, encordec, time, date)
    encryption_decryption.database.add_one(original=original, translated=translated, encordec=encordec, time=time, our_date=date)
    return '', 204


# Delete previous records.
@app.route('/database', methods=['DELETE'])
def delete_records(id_to_delete: str):
    """Deleting from database"""
    encryption_decryption.database.delete_one(id=id_to_delete)
    logging.debug("record deleted")
    return '', 204


# Get between queried dates.
@app.route('/queried', methods=['POST'])
def post_queried():
    """Getting dates from user"""
    encryption_decryption.dates_to_query.append(request.get_json())
    logging.debug("Received dates to query")
    start = encryption_decryption.dates_to_query[len(encryption_decryption.dates_to_query) - 1]["Start"]
    end = encryption_decryption.dates_to_query[len(encryption_decryption.dates_to_query) - 1]["End"]
    between_dates = encryption_decryption.database.query_between_two_days(start_date=start, end_date=end)
    encryption_decryption.queried_dates.clear()
    encryption_decryption.queried_dates.append(between_dates)
    return '', 204


# Return between queried dates.
@app.route('/queried')
def get():
    """Returning the dates"""
    # Turning grid into a string.
    database = json.dumps(encryption_decryption.queried_dates)
    formatted_database = re.sub(r"[\[\]]", "", database)
    # Return results.
    return json.dumps(formatted_database)

if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_database')