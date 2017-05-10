from flask import Flask
from flask import render_template
# if we run using python app.py, the namespce will be main.
# If we import it it will be app
app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="Shrimpley"):
    return render_template('index.html', name=name)


@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    if '.' in num1:
        num1 = float(num1)
    else:
        num1 = int(num1)
    if '.' in num2:
        num2 = float(num2)
    else:
        num2 = int(num2)

    context = {'num1': num1, "num2": num2}
    return render_template('add.html', **context)

app.run(debug=True)
