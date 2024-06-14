from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post-data', methods=['POST'])
def receive_data():
    data = request.json
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    response = {
        "status": "success",
        "temperature_received": temperature,
        "humidity_received": humidity
    }
    print(f"Received data - Temperature: {temperature}, Humidity: {humidity}")
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

