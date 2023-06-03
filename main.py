from flask import Flask, request, jsonify

app = Flask(__name__)
data = None  # This will store the last stored JSON data

@app.route('/api/data', methods=['POST'])
def store_data():
    json_data = request.get_json()  # Get the JSON data from the request
    global data
    data = json_data  # Update the last stored JSON data
    return jsonify({'message': 'Data stored successfully'})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run()
