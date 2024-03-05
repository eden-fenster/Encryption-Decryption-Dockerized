#!/usr/bin/env python3
"""Database storage object"""
import logging
import sys
from typing import List
from log_database import Database

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Storage:
    def __init__(self, directory: str, database_name: str):
        """Creating storage for database and JSON lists that will be returned"""
        # Creating the database.
        sys.path.append(f"/encryption_decryption_database_directory/{directory}/")
        from create_database import create
        create(directory=f'{directory}', database_name=f'{database_name}')
        logging.debug("created")
        # Variables.
        self._responses: List[dict] = []
        self._dates_to_query: List[dict] = []
        self._queried_dates: List[str] = []
        self._db = Database(directory=f'{directory}', database_name=f'{database_name}')

    @property
    def responses(self) -> List[dict]:
        """Return responses"""
        return self._responses

    @property
    def dates_to_query(self) -> List[dict]:
        """Return dates to query"""
        return self._dates_to_query

    @property
    def queried_dates(self) -> List[str]:
        """Return queried dates"""
        return self._queried_dates

    @property
    def database(self):
        """Return database"""
        return self._db
