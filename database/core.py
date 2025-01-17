from database.CRUD import CRUDInterface
from database.models import db, History

db.connect()
db.create_tables([History])

crud = CRUDInterface()


if __name__ == "__main__":
    crud.create()
    crud.retrieve()
    db.close()
