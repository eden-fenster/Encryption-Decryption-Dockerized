import requests
from flask import Flask, render_template, request, render_template_string
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = Flask(__name__)


PROCESSOR_SERVER: str = "encryption_decryption_processor"
PROCESSOR_PORT: str = "8000"

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
    pattern = request.form.get('pattern')
    # If pattern > 26, print error message.
    if len(pattern) > 26:
        logging.error(f"Pattern {pattern} is too long, exiting program...")
        return render_template('results.html') + render_template_string("the pattern was too long and therefore invalid")
    logging.debug(f"Input is {input} \n Pattern is {pattern} \n Encrypt or Decrypt ? {encordec}")
    # Put into dict.
    logging.debug("Putting into the dictionary to send")
    dict_to_send: dict = {'Input': input, 'Encrypt or Decrypt ?': encordec, 'Pattern': pattern}
    # Sent to processor.
    requests.post(f'http://{PROCESSOR_SERVER}:{PROCESSOR_PORT}/translate', json=dict_to_send, timeout=10)
    logging.debug("Sent to processor")
    # Translate.
    get_response = requests.get(f'http://{PROCESSOR_SERVER}:{PROCESSOR_PORT}/translated', timeout=10)
    logging.debug("Got Response from processor")
    # Return response.
    response = get_response.json()
    if not response:
        raise SystemError('Unable to get info')
    logging.debug(f"Getting and returning response {get_response} from processor")
    return render_template('results.html', Title='Results',
                           Content='Translation has been successful:\n') + render_template_string(response)


if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_web')
