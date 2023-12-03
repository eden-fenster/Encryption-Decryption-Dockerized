from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class EncryptionDecryptionDatabaseRecord(Base):
    __tablename__ = 'encryption_decryption_records'

    id = Column(Integer, primary_key=True)
    original_text = Column(String)
    translated_text = Column(String)

    def __repr__(self):
        return "<EncryptionDecryptionDatabase(original_text='%s', translated_text='%s')>" % (
            self.original_text, self.translated_text)


class EncryptionDecryptionDatabase:
    def __init__(self, data_base_file_name: str = 'sqlite:///encryption_decryption_records.db'):
        self._engine = create_engine(data_base_file_name, echo=False)
        Base.metadata.create_all(self._engine)
        Session = sessionmaker(bind=self._engine)
        self._session = Session()

    def add_one(self, original_text: str, translated_text: str):
        record_to_add = EncryptionDecryptionDatabaseRecord(original_text=original_text,
                                                           translated_text=translated_text)
        self._session.add(record_to_add)
        self._session.commit()

    def show_all(self):
        Query = self._session.query(EncryptionDecryptionDatabaseRecord).order_by(EncryptionDecryptionDatabaseRecord.id)
        record_list = Query.all()
        for record in record_list:
            print(record)
