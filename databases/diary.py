#!/usr/bin/env python
from peewee import *
"""Full peewee library"""
from collections import OrderedDict

import datetime

db = PostgresqlDatabase('diary')


def add_entry():
    """Add an entry"""


def view_entries():
    """View previous entries"""


def delete_entry(entry):
    """Delete an entry"""


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
])

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
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
            # dunder doc is the function's docstring.
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()



if __name__ == '__main__':
    initialise()
    menu_loop()
