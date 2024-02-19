import requests
from flask import Flask, render_template, request, render_template_string
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

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
    input = request.form.get('input')
    encordec = request.form.get('encordec')
    logging.debug(f"Input is {input} \n {encordec}")
    # Put into dict.
    logging.debug("Putting into the dictionary to send")
    dict_to_send: dict = {'Input': input, 'Encrypt or Decrypt ?': encordec}
    # Sent to processor.
    requests.post('http://encryption_decryption_processor:8000/translate', json=dict_to_send, timeout=10)
    logging.debug("Sent to processor")
    # Translate.
    get_response = requests.get('http://encryption_decryption_processor:8000/translated', timeout=10)
    logging.debug("Got Response from processor")
    # Return response.
    response = get_response.json()
    logging.debug("Printing response")
    return render_template('results.html', Title='Results',
                           Content='Translation has been successful:\n') + render_template_string(response)


if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_web')
