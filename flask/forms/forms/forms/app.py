import json

from flask import (Flask, request, render_template,
                   redirect, url_for, make_response,
                   flash)

from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'dkjwqbvhb3hbc£$^£@%^Crwrgev25£^5632TVgtreqg$%3635'


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS
        )


@app.route('/save', methods=['POST'])
def save():
    flash('All saved. Looking good')
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(dict(request.form.items())))
    return response


app.run(debug=True)
