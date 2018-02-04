from peewee import *


db = SqliteDatabase('People.db')


class Person(Model):
    name = CharField(max_length=30)
    year = SmallIntegerField()
    male = BooleanField()

    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([Person])
