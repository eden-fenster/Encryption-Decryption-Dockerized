#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-06-20
Purpose: encryption_decryption
"""

# --------------------------------------------------
import argparse
import os
from methods.dictionary import Create
from methods.text import Translate
from encryption_decryption_record_database_odbc import EncryptionDecryptionDatabase as Database

db = Database()


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='encryption_decryption',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text',
                        metavar='Input text')

    parser.add_argument('transformation',
                        help='Transformation pattern',
                        metavar='Transformation pattern')

    parser.add_argument('-e',
                        '--encrypt',
                        help='encrypt text',
                        dest='encrypt',
                        default=True,
                        action='store_true')

    parser.add_argument('-d',
                        '--decrypt',
                        help='decrypt text',
                        dest='encrypt',
                        default=True,
                        action='store_false')

    parser.add_argument('-o',
                        '--outfile',
                        help='Write Dict to file',
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.transformation):
        args.transformation = open(args.transformation).read().rstrip()

    return args


def main() -> None:
    args = get_args()
    text: str = args.text
    transformation_pattern: str = args.transformation
    encrypt: bool = args.encrypt
    outfile = args.outfile

    dictionary: dict = Create.create_dictionary(transformation_pattern=transformation_pattern, encrypt=encrypt)

    if outfile:
        out_fh = open(outfile, 'wt')
        out_fh.write(str(dictionary))
        out_fh.close()

    translated_text: str = Translate.translate_text(text_to_translate=text, dictionary=dictionary)
    db.add_one(text, translated_text)
    db.show_all()
    print(translated_text)


if __name__ == '__main__':
    main()
