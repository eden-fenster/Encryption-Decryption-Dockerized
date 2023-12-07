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
    logging.debug("Loading homepage")
    return render_template('index.html')


@app.route('/fight', methods=['GET', 'POST'])
def fight():
    """The actual fight"""
    # Input the input + encrypt/decrypt.
    # Put into dict.
    # Sent to processor.
    # Fight !


if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_web')
