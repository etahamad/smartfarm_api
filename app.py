import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
data = None  # This will store the last stored JSON data

@app.route('/', methods=['POST'])
def store_data():
    json_data = request.get_json()  # Get the JSON data from the request
    global data
    data = json_data  # Store the JSON data
    return jsonify({'message': 'Data stored successfully'})

@app.route('/', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
