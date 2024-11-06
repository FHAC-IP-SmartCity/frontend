# frontend

1. Data Ingestion (Pipeline Start)
Python with pySerial continuously reads data from the sensors over UART.
Trigger: This part of the pipeline is constantly running, capturing data as it comes in from the sensors.
Optional Real-Time Trigger with Message Broker:
If using Apache Kafka or RabbitMQ, the ingested data is pushed to a message broker immediately after processing.
Kafka/RabbitMQ ensures the data is continuously streamed into the next stages of the pipeline in real time.
2. Data Processing
Python scripts process the data by decoding, cleaning, and transforming it into a structured format (e.g., JSON).
Trigger: This processing happens immediately after ingestion, so it’s a continuous process. As each new data point is read from UART, it’s immediately parsed and transformed.
3. Data Storage (InfluxDB)
Processed data is then stored in InfluxDB, where each new data point is written to the database as soon as it’s ready.
Trigger: This step is also triggered automatically by the continuous data flow. Each new data point is written to the database in real time or near-real-time intervals (e.g., every few seconds).
If Kafka/RabbitMQ is used, a consumer service will pull data from the broker and write it into InfluxDB.
4. Data Visualization (Dashboard)
Grafana is set up with a direct connection to InfluxDB, allowing it to query the latest data.
Automatic Refresh in Grafana: Grafana’s auto-refresh settings ensure that it re-queries InfluxDB at a specified interval (e.g., every 5 seconds or every 5 minutes), displaying the latest data points on the dashboard.
