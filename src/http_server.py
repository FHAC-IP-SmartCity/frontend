
from flask import Flask, jsonify
from flask import request,render_template
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
        if 'id' in data and 'value' in data:
            #isinstance(data['id'], int) and
            #isinstance(data['value'], str)
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

# for JSON structure in webpage
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_buffer), 200

# for HTML structure in webpage
# @app.route('/data', methods=['GET'])
# def get_data():
#     return render_template('data.html', data=data_buffer)


def insert_into_database(record_id, value):
    """Insert data into the PostgreSQL database based on the id."""
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Determine the target table based on the id
        table_name = None
        if   record_id == 106:
            table_name = "noise_sensor"
        elif record_id == 110:
            table_name = "temperatur_sensor"
        elif record_id == 111:
            table_name = "gas_sensor"
        elif record_id == 112:
            table_name = "feuchtigkeit_sensor"
        elif record_id == 113:
            table_name = "luftdruck_sensor"
        elif record_id == 120:
            table_name= "rfid_sensor"
        elif record_id == 121:
            table_name= "rfid_sensor"
        elif record_id == 122:
            table_name= "rfid_sensor"
        elif record_id == 130:
            table_name = "park_sensor"
        elif record_id == 131:
            table_name = "park_sensor"
        elif record_id == 132:
            table_name = "park_sensor"
        elif record_id == 133:
            table_name = "park_sensor"
        elif record_id == 140:
            table_name = "motion_sensor"
        elif record_id == 141:
            table_name = "motion_sensor"
        elif record_id == 150:
            table_name = "light_sensor"
        else:
            print(f"Unhandled ID: {record_id}")
            return  # Optionally log or handle unrecognized IDs

        # Insert into the determined table
        if table_name:
            cursor.execute(f"INSERT INTO {table_name} (id, value) VALUES (%s, %s)", (record_id, value))
            connection.commit()
            print(f"Data inserted into {table_name}: id={record_id}, value={value}")

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