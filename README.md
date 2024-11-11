Introduction
This project is a dashboard for displaying real-time data from various sensors. The data pipeline involves data ingestion, processing, storage, and visualization to provide a comprehensive view of sensor data.

Project Phases and Tools
Phase 1: Initial Setup and Hardware Integration
Goal: Establish a reliable connection between the sensors and your computer, ensuring data can be read through UART.

Tools:

UART: Hardware communication protocol for data transfer.
Python (PySerial): Python library to handle UART serial communication, read sensor data, and process it in real-time.
Phase 2: Data Collection and Preprocessing
Goal: Collect data from sensors, parse it, and prepare it for storage.

Tools:

PySerial: Continuously reads and buffers incoming serial data.
Python Script: Parses and processes raw data into a structured format (e.g., JSON or a dictionary format).
Logging/Debugging: Use Python’s built-in logging or debugging tools (e.g., print statements or logging library) to validate that data is being received correctly.
Phase 3: Database Setup and Data Storage
Goal: Store parsed data efficiently for real-time access by the dashboard.

Tools:

InfluxDB: A time-series database optimized for real-time data. It allows you to store data with timestamps and retrieve it quickly for visualization.
InfluxDB Python Client: Facilitates the connection and interaction with InfluxDB directly from your Python script.
Phase 4: Real-Time Data Visualization
Goal: Visualize sensor data in real-time on a user-friendly dashboard.

Tools:

Grafana: Visualization tool that connects to InfluxDB, offering real-time dashboards and customizable widgets to represent data (e.g., counters for parking spots).
Grafana Data Source (InfluxDB): Grafana’s native support for InfluxDB allows seamless integration, making it easier to pull data directly for visualization.
Phase 5: Testing and Optimization
Goal: Test the full setup, optimize for performance, and handle any potential issues (like data loss or slow updates).

Tools:

Logging and Monitoring: Python logging for any issues in the data pipeline and Grafana alerts to monitor data thresholds.
Grafana Query Optimization: Fine-tune Grafana queries to ensure optimal performance.
InfluxDB Configuration: Adjust retention policies and indexing in InfluxDB for efficiency.
Phase 6: Deployment and Maintenance
Goal: Deploy the project for continuous operation, either locally or on a cloud/server environment, and set up mechanisms for long-term maintenance.

Tools:

Docker (optional): Containerize the Python script, InfluxDB, and Grafana setup for easier deployment and consistency across environments.
System Monitoring Tools: Set up monitoring to ensure that all components are running smoothly, and configure alerts for any service interruptions.
Automated Restart (e.g., cron job or service scripts): Ensure the script restarts automatically if interrupted, particularly on a remote server.
