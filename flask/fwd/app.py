from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    list = ['fish', 'monkey', 'cattington']
    return render_template('name.html', list=list)


@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return f'<h1>Your browser is {user_agent}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
