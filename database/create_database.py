#!/usr/bin/env python3
"""Creating a database"""
import logging
import os
import sqlite3

# pylint: disable=invalid-name
# pylint: disable=logging-fstring-interpolation

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def create(directory: str, database_name: str):
    """Creating a database"""
    full_path = os.path.join(directory, database_name)
    conn = sqlite3.connect(f'{full_path}.db', check_same_thread=False)
    c = conn.cursor()
    command = f"""CREATE TABLE IF NOT EXISTS {database_name} (
    original text,
    translated text,
    time text,
    date timestamp
    )"""
    c.execute(command)
    conn.commit()
    logging.debug(f"Database created in {full_path}")