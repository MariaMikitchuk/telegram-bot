from typing import Dict, List, TypeVar

from peewee import ModelSelect

from .models import History, db

T = TypeVar("T")


def _store_data(database: db, data: List[Dict], model: T = History) -> None:
    with database.atomic():
        model.insert_many(data).execute()


def _retrieve_all_data(database: db, columns: List[History], model: T = History) -> \
        ModelSelect:
    with database.atomic():
        response = model.select(*columns)
    return response


class CRUDInterface:
    @staticmethod
    def create(data: List[Dict]) -> None:
        _store_data(db, data)

    @staticmethod
    def retrieve(columns: List[History]) -> ModelSelect:
        return _retrieve_all_data(db, columns)



