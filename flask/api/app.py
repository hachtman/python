from flask import Flask

import models
from resources.courses import courses_api
from resources.reviews import reviews_api

app = Flask(__name__)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')


app.config.update(
    DEBUG=True,
    SECRET_KEY='verysecretsecretkeysecret'
)


@app.route('/')
def hello_world():
    return 'hello_world'


if __name__ == '__main__':
    models.initialize()
    app.run()

# Potentially use this to create the app allows clean reconfiguring.
# Would need Blueprint?
# def create_flask_app(config=None):
#     app = Flask(__name__)
#     return app
