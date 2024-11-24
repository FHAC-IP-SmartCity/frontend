# frontend-development

## Introduction
Follow the instructions below to initialize and start the project.
It was created for the Smart City Demonstrator project at Aachen University of Applied Sciences

## Phase 1: Data Ingestion 
### Goal: 
Establish a system to receive sensor data from the Proto app via HTTP POST requests in JSON format (or another format, as determined with the backend team).
### Tasks: 
1. Set up an HTTP server to receive incoming data.
2. Validate incoming JSON packets for: Completeness, Correctness
3. Temporarily store the raw or validated data: 
   - In memory
   - in a shared folder (to be determined).
### Tools: 
- **[Flask](https://flask.palletsprojects.com/):** A lightweight Python framework for hosting the HTTP server.
  - Preferred over Node.js to keep the project fully in Python.
- **[Proto.exe]:** For testing the POST request functionality.  
### Outcome: 
- JSON packets are successfully received and ingested.
- Data is validated and ready for the preprocessing phase.

## Phase 2: Data Preprocessing 
### Goal: 
Clean and prepare the ingested data for storage and visualization. (idea for dashboard). 
### Tasks: 
- Parse and validate the data structure (e.g., check for required fields like `id` and `value`). 
- Transform the data if necessary (e.g., convert types, handle missing values). 
- Log invalid or malformed packets for debugging.
### Tools: 
- Python (native JSON libraries): To parse, validate, and transform JSON packets. 
- Pandas: For transforming JSON into tabular data, if needed. 
- Logging Framework: Capture any errors or invalid data for debugging.
### Outcome:
Cleaned and validated data ready for database insertion or analysis. 

## Phase 3: Data  Storage
### Goal: 
Store data in a PostgreSQL database for persistent and structured storage.
### Tasks:
- Create a PostgreSQL account and database schema to store ingested data.
- Develop a .yml file for Docker to streamline the setup and execution of PostgreSQL.
- Write scripts to insert preprocessed data into the database
### Tools: 
- PostgreSQL: For data storage
- Docker: To manage the PostgreSQL instance using containers
### Steps: 
1. Pull the PostgreSQL Docker image:
   ```bash
   docker pull postgres
   ```
2. Start the PostgreSQL service:
   ```bash
   docker-compose up -d
   ```
### Outcome: 
Data is securely stored in PostgreSQL, ready for analysis and visualization.

## Phase 4: Data Analysis and Visualization
### Goal:
Analyze the stored data and provide meaningful visualizations through a Grafana Dashboard.
### Tasks:
- Set up Grafana to connect to the PostgreSQL database.
- Define and calculate key metrics for visualization.
- Create custom dashboards to display important insights
### Tools:
- Grafana: To create and manage dashboards.
### Steps:
1. Pull the Grafana Docker container:
   ```bash
   docker pull grafana/grafana
   ```
2. Run the Grafana Docker container:
   ```bash
   docker run -d -p 3000:3000 --name=grafana grafana/grafana
   ```
3. Connect Grafana to the PostgreSQL data source:
- Open http://localhost:3000 in a browser.
- Add PostgreSQL as a data source (Configuration > Data Sources).
- Provide the connection details (host, database name, username, password).
4. Create dashboards:
### Outcome:
Real-time and historical data are visualized in Grafana dashboards for easy analysis.

## Phase 5: Deployment 
### Goal:
Deploy the project, making it accessible for end-users or stakeholders.
### Tasks:
Use Docker Compose to orchestrate the Flask server, PostgreSQL database, and Grafana.
### Tools: 
Docker Compose: To manage multi-container deployment.
### Steps:
### Outcome: 
A fully deployed system with ingestion, preprocessing, storage, analysis, and visualization.

## Useful Scripts
1. Start all services:
   ```bash
   docker-compose up -d
   ```
2. Stop all services:
   ```bash
   docker-compose down
   ```
3. View logs (if needed):
   ```bash
   docker-compose logs
   ```


