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


@app.route('/encryptordecrypt', methods=['GET', 'POST'])
def encrypt_decrypt():
    """Getting the input to encrypt/decrypt"""
    # Input the input + encrypt/decrypt.
    # Put into dict.
    # Sent to processor.


if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_web')
