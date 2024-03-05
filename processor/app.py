from methods.dictionary import Create
from methods.text import Translate
import json
import re
import time
from datetime import datetime
from typing import List
from processor_storage import Storage

import requests
from flask import Flask, render_template, request
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = Flask(__name__)

# Storing our lists
input_to_return: Storage = Storage()

DATABASE_SERVER: str = "encryption_decryption_database"
DATABASE_PORT: str = "3000"

# pylint: disable=consider-using-f-string

# pylint: disable=logging-fstring-interpolation


# Input to translate
@app.route('/translate', methods=['POST'])
def input_first():
    """Input the input + encrypt/decrypt"""
    # Recieving input.
    logging.debug("Loading, recieving input ")
    input_to_return._input.append(request.get_json())
    logging.debug(f"Received {input_to_return._input}")
    # Getting current date and time
    logging.debug("Getting current date and time")
    current_time = datetime.now()
    time_string_for_print = current_time.strftime("%m/%d/%Y, %H:%M:%S")
    time_string = current_time.strftime("%Y-%m-%d %H:%M")
    start_time = time.time()
    # Create dictionary.
    dictionary: dict = Create.create_dictionary(transformation_pattern=input_to_return._input[len(input_to_return._input) - 1]["Pattern"],
                                                 encrypt=input_to_return._input[len(input_to_return._input) - 1]["Encrypt or Decrypt ?"])
    logging.debug(f"dictionary from {input_to_return._input[len(input_to_return._input) - 1]["Pattern"]} created")
    # Sending it to method that will translate it.
    translated_text: str = Translate.translate_text(text_to_translate=input_to_return._input[len(input_to_return._input) - 1]["Input"],
                                                    dictionary=dictionary)
    end_time = time.time()
    total_time = end_time - start_time
    total_time_string: str = str("%.2f" % total_time)
    logging.debug(f"{input_to_return._input[len(input_to_return._input) - 1]["Input"]} has been translated to -> {translated_text}")
    # Adding input_to_return._translated_input input to list.
    input_to_return._translated_input.append(translated_text)
    # adding input + dictionary + time to database.
    database_record: dict = {"Original": input_to_return._input[len(input_to_return._input) - 1]["Input"], 
                             "Translated": translated_text,
                             "Time": total_time_string, "Date": time_string}
    requests.post(f"http://{DATABASE_SERVER}:{DATABASE_PORT}/database",
                  json=database_record, timeout=10)
    logging.debug(f"Added record {database_record} to database")
    # clearing list.
    input_to_return._input.clear()

    return '', 204

# Return input_to_return._translated_input input
@app.route('/translated')
def return_translated():
    """Return translated input"""
    # Return results.
    printing_translation = json.dumps(input_to_return._translated_input)
    logging.debug(f"Cleaning up {printing_translation} from unneeded things")
    formatted_translation = re.sub(r"[\[\]]", "", printing_translation)
    # clearing list
    input_to_return._translated_input.clear()
    return json.dumps(formatted_translation)


if __name__ == "__main__":
    app.run(debug=True, host='encryption_decryption_processor')
