from flask import Flask, jsonify, request
import json

app = Flask(__name__)

DATA_FILE = 'data.json'

def read_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

@app.route('/weatherdata', methods=['POST'])
def create_weather_data():
    weather_data = request.get_json()

    write_data(weather_data)

    response = {'message': 'Weather data created successfully'}
    return jsonify(response), 201

@app.route('/weatherdata', methods=['GET'])
def get_weather_data():
    data = read_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
