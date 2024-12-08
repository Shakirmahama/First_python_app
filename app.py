from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.json  # Get JSON data from Flutter
    num1 = data.get('num1', 0)  # Get first number
    num2 = data.get('num2', 0)  # Get second number
    result = num1 + num2  # Calculate sum
    return jsonify({'sum': result})  # Return the result as JSON

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
