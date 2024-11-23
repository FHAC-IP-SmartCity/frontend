# Phase 1: Data Ingestion

## Goal
Establish a system to receive sensor data from the Proto app via HTTP POST requests in JSON format (or another format, as determined with the backend team).

---
## Tasks
1. Set up an HTTP server to receive incoming data.
2. Validate incoming JSON packets for:
   - Completeness
   - Correctness
3. Temporarily store the raw or validated data:
   - In memory
   - in a shared folder (to be determined).
   - 
---
## Tools
- **[Flask](https://flask.palletsprojects.com/):** A lightweight Python framework for hosting the HTTP server.
  - Preferred over Node.js to keep the project fully in Python.
- **[Proto.exe]:** For testing the POST request functionality.

---
## Outcome
- JSON packets are successfully received and ingested.
- Data is validated and ready for the preprocessing phase.
