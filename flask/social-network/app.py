from flask import (Flask, g, render_template, flash, redirect, url_for)

from flask_login import (LoginManager,
                         logout_user,
                         login_user,
                         current_user,
                         login_required)
from flask_bcrypt import check_password_hash

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
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the db connection after each request"""
    g.db.close()
    return response


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        flash('Successfully registered', 'success')
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Your email or password doesn't match", "error")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You've been logged in.", "success")
                return redirect(url_for('index'))
            else:
                flash("Your email or password doesn't match", "error")
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out', 'success')
    return redirect(url_for('index'))


@app.route('/')
def index():
    stream = models.Post.select().limit(100)
    return render_template('stream.html', stream=stream)

@app.route('/stream')
@app.route('/stream/<username>')
def stream(username=None):
    template = 'stream.html'
    if suername and username != current_user.username:
        user = models.User.select().where(models.User.username**username)
    else:
        stream = current_user.get_stream().limit(100)
        user = current_user
    if username:
        template = 'user_stream.html'
    return render_template(template=template, stream=stream, user=user)

@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = forms.PostForm()
    if form.validate_on_submit():
        models.Post.create(user=g.user._get_current_object(),
                           content=form.content.data.strip())
        flash("Message posted! Thanks.", "success")
        return redirect(url_for('index'))
    return render_template('post.html', form=form)



if __name__ == '__main__':
    models.initialize()
    # models.User.create_user(
    #     username='jackfuller',
    #     email='jack@fuller.com',
    #     password='freemonkey',
    #     admin=True
    # )
    app.run(debug=DEBUG, port=PORT, host=HOST)
