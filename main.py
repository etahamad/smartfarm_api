import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
data = None  # This will store the last stored JSON data

@app.route('/api/data', methods=['POST'])
def store_data():
    json_data = request.get_json()  # Get the JSON data from the request
    json_response = send_request_to_api(json_data)  # Send the request to the target API and get the JSON response
    global data
    data = json_response  # Update the last stored JSON data
    return jsonify({'message': 'Data stored successfully'})

def send_request_to_api(json_data):
    url = 'https://etahamad-new-plant-disease-detection.hf.space/run/predict'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=json_data, headers=headers, proxies={})  # Disable the proxy configuration
    return response.json()  # Return the JSON response

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
