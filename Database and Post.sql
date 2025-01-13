--database configuration using docker 
in cmd:
.\frontend>docker exec -it Smart-City psql -U ip -d smartcitydb
proto send -d http://127.0.0.1:3000/data -i 5 -v "Hello"
proto listen -s COM3 --web -d http://127.0.0.1:3000/data

--SQL commands 01.12.2024 --to be updated when new command is required 
smartcitydb=# CREATE TABLE smartcity (id INTEGER, value VARCHAR(200));
ALTER TABLE smartcity
ADD COLUMN time TIMESTAMP;



--Postgres db in grafana configuration 
host:  postgres:5432
user:  ip
password: smartcity
database: smartcitydb
tsl mode: disable



DATENBANK ertellen:
CREATE TABLE light_sensor(id INTEGER , value boolean , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP );
CREATE TABLE light_intens_sensor(id INTEGER , value boolean , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE noise_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE temperatur_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE gas_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE feuchtigkeit_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE luftdruck_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE motion_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE RFID_sensor(id INTEGER, value INTEGER , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE park_sensor(id INTEGER, value boolean , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE park_zahler_sensor(id INTEGER, value INTEGER , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE RFID_bus_sensor(id INTEGER, value boolean , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);