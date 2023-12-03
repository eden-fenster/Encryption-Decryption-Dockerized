import sqlite3

# Create a table
# conn = sqlite3.connect('encryption_decryption_records.db')

# Create a cursor
# c = conn.cursor()
# c.execute("""CREATE TABLE encryption_decryption_records (
#   original_text text,
#   translated_text text
#   )""")
# conn.commit()
# conn.close()


# Add a new record to the table
class EncryptionDecryptionDatabase:

    def __init__(self, database_path: str):
        self._connection = sqlite3.connect(database_path)
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("SELECT rowid, * FROM encryption_decryption_records")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def add_one(self, original: str, transformed: str):
        self._cursor.execute("INSERT INTO customers VALUES (?, ?)", (original, transformed))
        self._connection.commit()
        self._connection.close()
