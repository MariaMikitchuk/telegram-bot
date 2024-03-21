from datetime import datetime

import peewee as pw


db = pw.SqliteDatabase('history.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta:
        database = db


class History(ModelBase):
    user_id = pw.CharField()
    message = pw.CharField()
    created_at = pw.DateTimeField()
