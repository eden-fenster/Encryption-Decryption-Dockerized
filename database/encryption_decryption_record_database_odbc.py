import pyodbc


# Add a new record to the table
class EncryptionDecryptionDatabase:

    def __init__(self, database_path: str = 'encryption_decryption_records.db'):
        self._connection = pyodbc.connect("Driver=SQLite;Database="f"{database_path}")
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("select rowid, * from encryption_decryption_records")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def add_one(self, original_text: str, translated_text: str):
        self._cursor.execute("insert into encryption_decryption_records (original_text, translated_text) values (?, ?)"
                             , original_text, translated_text)
        self._connection.commit()
