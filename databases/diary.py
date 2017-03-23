#!/usr/bin/env python
from collections import OrderedDict
import datetime
import sys
import os
from termcolor import colored, cprint

from peewee import *
"""Full peewee library"""

db = PostgresqlDatabase('diary')


def add_entry():
    """Add an entry"""
    print("Enter your entry. Press 'CTRL D' when finished.")
    data = sys.stdin.read().strip()

    if data:
        if input("Save entry? [Y/N] ").lower() != 'n':
            Entry.create(content=data)
            print("**********\nSaved succesfully.\n**********")


def view_entries(search_query=None):
    """View previous entries"""

    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query)).order_by(
                                Entry.timestamp.desc()
                                )
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear_screen()
        print(timestamp)
        print('=' * len(timestamp))
        cprint(entry.content, 'green')
        print('=' * len(timestamp) + '\n\n')
        print('(N) for next entry, (D) delete entry, (q) return to main menu')

        next_action = input("Action: (N/q)").lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def search_entries():
    """Search entries for a string"""
    view_entries(input("Search query: "))


def delete_entry(entry):
    """Delete an entry"""
    if input("Are you sure? (y/N) ").lower() == 'y':
        entry.delete_instance()
        cprint('ENTRY REMOVED.', 'red')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
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
        clear_screen()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
            # dunder doc is the function's docstring.
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear_screen()
            menu[choice]()



if __name__ == '__main__':
    initialise()
    menu_loop()
