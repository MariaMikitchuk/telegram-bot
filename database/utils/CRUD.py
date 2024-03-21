from typing import Dict, List, TypeVar

from peewee import ModelSelect

from database.common.models import ModelBase
from ..common.models import db

T = TypeVar("T")


def _store_data(database: db, model: T, *data: List[Dict]) -> None:
    with database.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(database: db, model: T, *columns: ModelBase) -> ModelSelect:
    with database.atomic():
        response = model.select(*columns)
    return response


class CRUDInterface:
    @staticmethod
    def create():
        return _store_data

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == "__main__":
    _store_data()
    _retrieve_all_data()
    CRUDInterface()
