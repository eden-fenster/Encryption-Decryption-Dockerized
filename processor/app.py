from methods.dictionary import Create
from methods.text import Translate
import json
import re
from typing import List

import requests
from flask import Flask, render_template, request
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

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
    # Create dictionary.
    transformation_pattern: str = 'hag'
    dictionary: dict = Create.create_dictionary(transformation_pattern=transformation_pattern,
                                                 encrypt=input_to_translate[len(input_to_translate) - 1]["Encrypt or Decrypt ?"])
    # Sending it to method that will translate it.
    translated_text: str = Translate.translate_text(text_to_translate=input_to_translate[len(input_to_translate) - 1]["Input"],
                                                    dictionary=dictionary)
    # Adding translated input to list.
    translated.append(translated_text)

    return '', 204

# Return translated input
@app.route('/translated')
def return_translated():
    """Return translated input"""
    # Return results.
    printing_translation = json.dumps(translated)
    logging.debug(f"Cleaning up {printing_translation} from unneeded things")
    formatted_translation = re.sub(r"[\[\]]", "", printing_translation)
    return json.dumps(formatted_translation)


if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_processor')
