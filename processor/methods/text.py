#!/usr/bin/env python3

class Translate:
    @staticmethod
    def translate_text(text_to_translate: str, dictionary: dict) -> str:
        new_text: str = ''
        for letter in text_to_translate:
            new_text += dictionary.get(letter, letter)
        return new_text
