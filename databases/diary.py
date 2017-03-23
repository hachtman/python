#!/usr/bin/env python
from peewee import *
import datetime

db = PostgresqlDatabase('diary')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    # timestamp

    class Meta:
        database = db


def initialise():
    """Create database and table if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""


def add_entry():
    """Add an entry"""


def view_entries():
    """View previous entries"""


def delete_entry(entry):
    """Delete an entry"""


if __name__ == '__main__':
    initialise()
    menu_loop()
