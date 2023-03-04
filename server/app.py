from flask import Flask, request, jsonify
from joblib import load

model = load('model/model.joblib')
app = Flask(__name__)
target_names = ['setosa', 'versicolor', 'virginica']


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([[
        data['sepal_length'],
        data['sepal_width'],
        data['petal_length'],
        data['petal_width'],
    ]])
    return jsonify({'flower_type': target_names[prediction[0]]})


if __name__ == '__main__':
    app.run()
