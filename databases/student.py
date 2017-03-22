from peewee import *
import psycopg2

# connection = psycopg2.connect(dbname='students', user='jackfuller', host='localhost')

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
            db.rollback()
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()


def return_top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Our current top student is: {0.username}.".format(return_top_student()))
