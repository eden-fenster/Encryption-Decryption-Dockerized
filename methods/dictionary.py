#!/usr/bin/env python3
from string import ascii_lowercase


class Create:
    @staticmethod
    def create_dictionary(transformation_pattern: str, encrypt: bool) -> dict:
        dictionary: dict = {}
        if encrypt:
            for i in range(0, len(transformation_pattern)):
                dictionary.update({ascii_lowercase[i]: transformation_pattern[i]})
        else:
            for i in range(0, len(ascii_lowercase)):
                dictionary.update({transformation_pattern[i]: ascii_lowercase[i]})
        return dictionary
