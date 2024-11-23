from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Create an in-memory buffer to temporarily store data
data_buffer = []

# Define the endpoint to receive data
@app.route('/data', methods=['POST'])
def receive_data():
    try:
        # Log the raw incoming data for debugging
        print("\nRaw request data:", request.data)

        # Parse the JSON data from the request
        data = request.json  # Use request.json to parse JSON payloads

        # Validate the JSON structure and data types
        if (
            'id' in data and 'value' in data and
            isinstance(data['id'], int) and
            isinstance(data['value'], str)
        ):
            # Store the valid data in the buffer
            data_buffer.append(data)

            print("Received valid data:", data)
            return jsonify({"status": "success"}), 200
        else:
            # 400 means invalid data format
            print("Invalid data format:", data)
            return jsonify({"error": "Invalid data format"}), 400

    except Exception as e:
        # Log unexpected errors and respond with a 500 status
        print("Error processing request:", str(e))
        return jsonify({"error": str(e)}), 500


# Run the server on port 3000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)