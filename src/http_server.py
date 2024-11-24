from flask import Flask, request, jsonify
import psycopg2

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    "dbname": "smartcitydb",
    "user": "ip",
    "password": "smartcity",
    "host": "localhost",  # Use "postgres" if running inside the same Docker network
    "port": 3021  # Port mapping from Docker Compose
}
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

            # Insert data into the database
            insert_into_database(data['id'], data['value'])

            return jsonify({"status": "success"}), 200
        else:
            # 400 means invalid data format
            print("Invalid data format:", data)
            return jsonify({"error": "Invalid data format"}), 400

    except Exception as e:
        # Log unexpected errors and respond with a 500 status
        print("Error processing request:", str(e))
        return jsonify({"error": str(e)}), 500


def insert_into_database(record_id, value):
    """Insert data into the PostgreSQL database."""
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Insert data into the table
        cursor.execute("INSERT INTO test (id, value) VALUES (%s, %s)", (record_id, value))
        
        # Commit the transaction
        connection.commit()

        print(f"Data inserted: id={record_id}, value={value}")

    except Exception as e:
        print("Database error:", str(e))
    finally:
        # Close the database connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

# Run the server on port 3000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)