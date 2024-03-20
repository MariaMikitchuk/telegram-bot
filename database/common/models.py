from datetime import datetime

import peewee as pw


db = pw.SqliteDatabase('history.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta:
        database = db


class History(ModelBase):
    function = pw.TextField()
    nutrient = pw.TextField()
    value = pw.IntegerField()
    dish = pw.TextField()