#!/usr/bin/env python3
"""Sudoku Solver - Database"""
import json
import logging
import re

from datetime import datetime
from database_storage import Storage

from flask import Flask, request

DATABASE_DIRECTORY: str = 'database'
DATABASE_NAME: str = 'sudoku_results'

app = Flask(__name__)

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# pylint: disable=invalid-name

# A class with all of our things
sudoku: Storage = Storage(directory=DATABASE_DIRECTORY, database_name=DATABASE_NAME)


# Returns the results
@app.route('/database')
def get_database():
    """Getting from database"""
    return json.dumps(sudoku.database.show_all())


@app.route('/database', methods=['POST'])
def add_to_database():
    """Adding to database"""
    # Adding to list.
    sudoku.responses.append(request.get_json())
    solution = sudoku.responses[len(sudoku.responses) - 1]["Solution"]
    time = sudoku.responses[len(sudoku.responses) - 1]["Time"]
    date = datetime.strptime(sudoku.responses[len(sudoku.responses) - 1]["Date"], '%Y-%m-%d %H:%M')
    # If of wrong type, raise value error.
    if not isinstance(solution, str):
        raise ValueError(f"Variable {solution} is of wrong type {type(solution)}")
    if not isinstance(time, str):
        raise ValueError(f"Variable {time} is of wrong type {type(time)}")
    if not isinstance(date, datetime):
        raise ValueError(f"Variable {date} is of wrong type {type(date)}")
    # Adding to database
    logging.debug("Solution -> %s \n Time -> %s \n Date -> %s", solution, time, date)
    sudoku.database.add_one(solution=solution, time=time, our_date=date)
    return '', 204


# Delete previous records.
@app.route('/database', methods=['DELETE'])
def delete_records(id_to_delete: str):
    """Deleting from database"""
    sudoku.database.delete_one(id=id_to_delete)
    logging.debug("record deleted")
    return '', 204


# Get between queried dates.
@app.route('/queried', methods=['POST'])
def post_queried():
    """Getting dates from user"""
    sudoku.dates_to_query.append(request.get_json())
    logging.debug("Received dates to query")
    start = sudoku.dates_to_query[len(sudoku.dates_to_query) - 1]["Start"]
    end = sudoku.dates_to_query[len(sudoku.dates_to_query) - 1]["End"]
    between_dates = sudoku.database.query_between_two_days(start_date=start, end_date=end)
    sudoku.queried_dates.clear()
    sudoku.queried_dates.append(between_dates)
    return '', 204


# Return between queried dates.
@app.route('/queried')
def get():
    """Returning the dates"""
    # Turning grid into a string.
    database = json.dumps(sudoku.queried_dates)
    formatted_database = re.sub(r"[\[\]]", "", database)
    # Return results.
    return json.dumps(formatted_database)

if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_database')