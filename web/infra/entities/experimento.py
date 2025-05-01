from infra.configs.base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column
import json
from json import JSONEncoder


class Experimento(Base):
    __tablename__ = "experimento"
    id = mapped_column(Integer, primary_key=True)
    click = mapped_column(Integer, nullable=False)
    visit = mapped_column(Integer, nullable=False)
    grupo = mapped_column(String, nullable=False)

    def __iter__(self):
        yield from [self.click, self.visit, self.grupo]

    def __str__(self):
        return json.dumps(dict(self), cls=JSONEncoder, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
