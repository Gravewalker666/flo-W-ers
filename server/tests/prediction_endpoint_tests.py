from app import app, target_names

test_data = {
    'data': [
        [5.8, 2.8, 5.1, 2.4],
        [6.0, 2.2, 4.0, 1.0],
        [5.5, 4.2, 1.4, 0.2],
        [7.3, 2.9, 6.3, 1.8],
        [5.0, 3.4, 1.5, 0.2]
    ],
    'target': [2, 1, 0, 2, 0]
}


def test_predict():
    client = app.test_client()
    for i in range(len(test_data['data'])):
        response = client.post('/predict', json={
            'sepal_length': test_data['data'][i][0],
            'sepal_width': test_data['data'][i][1],
            'petal_length': test_data['data'][i][2],
            'petal_width': test_data['data'][i][3],
        })
        assert response.status_code == 200
        assert response.json['flower_type'] == target_names[test_data['target'][i]]
