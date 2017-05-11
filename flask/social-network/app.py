from flask import (Flask, g, render_template, flash, redirect, url_for)
from flask_login import LoginManager

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'averysere312854c9n3t4inuc2fgu5ygtcy2gnfu2yu5£$^cc3455'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to the db before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the db connection after each request"""
    g.db.close()
    return response


if __name__ == '__main__':
    models.initialize()
    # models.User.create_user(
    #     username='jackfuller',
    #     email='jack@fuller.com',
    #     password='freemonkey',
    #     admin=True
    # )
    app.run(debug=DEBUG, port=PORT, host=HOST)
