from typing import List

import requests
from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# pylint: disable=logging-fstring-interpolation

# Opening page to input details.
# List to store received input.
input_to_translate: List[dict] = []
# List to store encrypted/decrypted input.
translated: List[str] = []


# Input to translate
@app.route('/translate', methods=['POST'])
def input_first():
    """Input the input + encrypt/decrypt"""
    # Recieving input.
    logging.debug("Loading, recieving input ")
    input_to_translate.append(request.get_json())
    logging.debug(f"Received {input_to_translate}")
    # Sending it to method that will translate it.
    # Adding translated input to list.

    return "Hello World"

# Return translated input
@app.route('/')
def return_translated():
    """Return translated input"""
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_processor')
