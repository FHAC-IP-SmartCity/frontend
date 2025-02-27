CREATE TABLE IF NOT EXISTS light_sensor_west(id INTEGER , value INT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP );
CREATE TABLE IF NOT EXISTS light_sensor_hbf(id INTEGER , value INT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP );
CREATE TABLE IF NOT EXISTS light_park_sensor(id INTEGER , value INT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS light_intens_sensor(id INTEGER , value INT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS temperatur_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS gas_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS feuchtigkeit_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS luftdruck_sensor(id INTEGER, value FLOAT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS RFID_sensor(id INTEGER, value INT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS park_sensor(id INTEGER, value boolean , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS park_zahler_sensor(id INTEGER, value INT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS RFID_bus_sensor(id INTEGER, value INT , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);