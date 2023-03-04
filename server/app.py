from flask import Flask
from joblib import load

model = load('model/model.joblib')
app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"


@app.route('/predict/<float:sepal_length>/<float:sepal_width>/<float:petal_length>/<float:petal_width>')
def predict(sepal_length, sepal_width, petal_length, petal_width):
    return str(model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0])


if __name__ == '__main__':
    app.run()
