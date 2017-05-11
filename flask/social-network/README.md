#Building a simple social network with python and Flask.

##Goals
To get comfortable with the Flask framework and test it against Django/DRF for an upcoming large scale web app that needs to make use of numpy, scipy and machine learning libraries.

This project draws heavily on the 'Build a social network with Flask' tutorial from Treehouse.

##Stack
Flask. The primary web server and framework for the project, Flask has great documentation and an active community. It also feels familiar (Express-like).

PeeWee, a great and insanely simple Python ORM. Check out this thread for a bit more info. https://www.reddit.com/r/Python/comments/4tnqai/choosing_a_python_ormpeewee_vs_sqlalchemy/

Postgres for the database. Can only connect to peewee with the help of the handy psycopg2 package.

flask-login. Provides session management and handles logging in and out. Provides the UserMixin parent class, which adds several attributes and a method.
http://flask-login.readthedocs.io/en/latest/#your-user-class

flask-bcrypt. Bcrypt implementation for Flask to handle password hashing.

flask-wtf. This package provides us with form implementation and CSRF protection. Includes a custom one time code with each submission.
