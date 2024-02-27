#!/usr/bin/env python3
"""Database storage object"""

from typing import List


class Storage:
    def __init__(self):
        """Creating storage for JSON lists that will be returned"""
        # Variables.
        # List to store input + instruction.
        self._input: List[dict] = []
        # List to store the returned results.
        self._translated_input: List[str] = []

    @property
    def input(self) -> List[dict]:
        """Return input"""
        return self._input

    @property
    def translated_input(self) -> List[str]:
        """Return string of results"""
        return self._translated_input