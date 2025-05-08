import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from infra.configs.base import Base

class DBConnectionHandler:
    def __init__(self):
        url = os.getenv('DATABASE_URL')
        self.__connection_string = url
        self.__engine = self.__create_database_engine()
        Base.metadata.create_all(bind=self.__engine)
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        ssesion_make = sessionmaker(bind=self.__engine)
        self.session = ssesion_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
