from peewee import *
import psycopg2

connection = psycopg2.connect(dbname='students', user='jackfuller', host='localhost')

db = PostgresqlDatabase('students')

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db


students = [
    {'username': 'james',
     'points': 3000},
    {'username': 'harold',
     'points': 3456},
    {'username': 'fishboy',
     'points': 4567},
    {'username': 'jonathan',
     'points': 12}
]


def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
