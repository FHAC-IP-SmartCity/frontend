
in cmd:
C:\Users\zergh\Documents\GitHub\frontend>docker exec -it Smart-City psql -U ip -d smartcitydb
psql (15.8 (Debian 15.8-1.pgdg120+1))
Type "help" for help.

smartcitydb=# CREATE TABLE test (id INTEGER, value VARCHAR(200));