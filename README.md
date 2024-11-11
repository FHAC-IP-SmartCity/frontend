# Near Real-Time Sensor Data Dashboard

This project provides a real-time dashboard for visualizing data from various sensors. The data pipeline consists of several phases including data ingestion, processing, storage, and visualization, offering a comprehensive overview of sensor data.

---

## Project Phases and Tools

### Phase 1: Initial Setup and Hardware Integration
**Goal**: Establish a reliable connection between sensors and the computer, ensuring data can be read via UART.

**Tools**:
- **UART**: Hardware communication protocol for data transfer.
- **Python (PySerial)**: Handles UART serial communication to read and process sensor data in real-time.

---

### Phase 2: Data Collection and Preprocessing
**Goal**: Collect, parse, and prepare sensor data for storage.

**Tools**:
- **PySerial**: Continuously reads and buffers incoming serial data.
- **Python Script**: Parses and structures raw data (e.g., JSON or dictionary format).

---

### Phase 3: Database Setup and Data Storage
**Goal**: Efficiently store parsed data for near real-time dashboard access.

**Tools**:
- **InfluxDB**: A time-series database optimized for real-time data, supporting fast retrieval.
- **InfluxDB Python Client**: Connects and interacts with InfluxDB directly from the Python script.

---

### Phase 4: Real-Time Data Visualization
**Goal**: Display sensor data in real-time on a user-friendly dashboard.

**Tools**:
- **Grafana**: Visualization tool with customizable widgets for data representation (e.g., counters for parking spots).
- **Grafana Data Source (InfluxDB)**: Native integration with InfluxDB for seamless data retrieval and visualization.

---

### Phase 5: Testing and Optimization
**Goal**: Test the setup, optimize performance, and address issues like data loss or slow updates.

**Tools**:
- **Logging and Monitoring**: Python logging for pipeline issues and Grafana alerts to monitor data thresholds.
- **Grafana Query Optimization**: Fine-tune Grafana queries for performance.
- **InfluxDB Configuration**: Adjust retention policies and indexing to enhance efficiency.

---

### Phase 6: Deployment and Maintenance
**Goal**: Deploy the project for continuous operation and establish maintenance mechanisms.

**Tools**:
- **Docker (optional)**: Containerize Python, InfluxDB, and Grafana for consistent and simplified deployment.
- **System Monitoring Tools**: Set up alerts for component interruptions and monitor service health.
- **Automated Restart**: Use cron jobs or service scripts to restart scripts automatically if interrupted.

---
