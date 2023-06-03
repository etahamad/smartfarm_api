from flask import Flask, request

app = Flask(__name__)
data = None  # This will store the last stored JSON data

@app.route('/api/data', methods=['POST'])
def store_data():
    json_data = request.get_json()  # Get the JSON data from the request
    global data
    data = json_data  # Update the last stored JSON data
    return 'Data stored successfully'

@app.route('/api/data', methods=['GET'])
def get_data():
    if data is not None and 'data' in data:
        return data['data'][0]  # Return the value at index 0
    else:
        return 'No data available'

if __name__ == '__main__':
    app.run()
