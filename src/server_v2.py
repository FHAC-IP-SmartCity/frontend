from flask import Flask, jsonify
from flask import request, render_template
import psycopg2
from collections import deque
import threading
import queue
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database configuration
DB_CONFIG = {
    "dbname": "prodDB",
    "user": "kunde",
    "password": "kunde",
    "host": "postgres",  # Use "postgres" if running inside the same Docker network
    "port": 5432 # Port mapping from Docker Compose
}

# Create an in-memory deque buffer to temporarily store data
data_buffer = deque(maxlen=10000)  # Automatically drop oldest records if full
data_queue = queue.Queue()  # Queue for background processing

# Table name mapping for record IDs
TABLE_NAME_MAP = {
    1100: "RFID_sensor",
    2210: "light_sensor_hbf",
    2220: "light_sensor_hbf",
    2230: "light_park_sensor",
    2240: "light_park_sensor",
    2250: "light_park_sensor",
    3110: "RFID_bus_sensor",
    3210: "light_sensor_west",
    3220: "light_sensor_west",
    3310: "park_zahler_sensor",
    4410: "light_intens_sensor",
    4511: "temperatur_sensor",
    4512: "gas_sensor",
    4513: "feuchtigkeit_sensor",
    4514: "luftdruck_sensor",
    #4610: "noise_sensor"
}

def get_table_name(record_id):
    return TABLE_NAME_MAP.get(record_id, None)

# Background worker for processing data
def data_worker():
    while True:
        record = data_queue.get()
        if record is None:  # Stop the worker
            break
        insert_into_database(record['id'], record['value'])

worker_thread = threading.Thread(target=data_worker, daemon=True)
worker_thread.start()

# Define the endpoint to receive data
@app.route('/', methods=['POST'])
@app.route('/data', methods=['POST'])
def receive_data():
    try:
        # Parse the JSON data from the request
        data = request.json

        # Validate the JSON structure and data types
        if 'id' in data and 'value' in data:
            logging.info("Received valid data: %s", data)

            # Add data to the queue for background processing
            data_queue.put(data)

            # Add data to the buffer for GET endpoint
            data_buffer.append(data)

            return jsonify({"status": "success"}), 200
        else:
            # Log invalid data format
            logging.warning("Invalid data format: %s", data)
            return jsonify({"error": "Invalid data format"}), 400

    except Exception as e:
        # Log unexpected errors and respond with a 500 status
        logging.error("Error processing request: %s", str(e))
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve buffered data
@app.route('/', methods=['GET'])
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(data_buffer)), 200

def insert_into_database(record_id, value):
    """Insert data into the PostgreSQL database based on the id."""
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Determine the target table based on the id
        table_name = get_table_name(record_id)
        if table_name:
            cursor.execute(f"INSERT INTO {table_name} (id, value) VALUES (%s, %s)", (record_id, value))
            connection.commit()
            logging.info(f"Data inserted into {table_name}: id={record_id}, value={value}")

    except Exception as e:
        logging.error("Database error: %s", str(e))
    finally:
        # Close the database connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

# Run the server on port 3000
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=3000, debug=True)
    finally:
        # Stop the worker thread gracefully
        data_queue.put(None)
        worker_thread.join()
