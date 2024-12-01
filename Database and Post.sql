--database configuration using docker 
in cmd:
.\frontend>docker exec -it Smart-City psql -U ip -d smartcitydb
proto send -d http://127.0.0.1:3000/data -i 5 -v "Hello"


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