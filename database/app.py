import requests
from flask import Flask, render_template, request
import logging

app = Flask(__name__)


# pylint: disable=logging-fstring-interpolation

# Opening page to input details.


# First player
@app.route('/')
def input_first():
    """Input the input + encrypt/decrypt"""
    logging.debug("Loading")
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_database')