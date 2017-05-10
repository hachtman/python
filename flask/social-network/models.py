import datetime

from peewee import *


DATABASE = PostgresqlDatabase('social-network.db')


class User(Model):
    username = Charfield(unique=True)
    email = Charfield(unique=True)
    password = Charfield(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)
