
in cmd:
C:\Users\zergh\Documents\GitHub\frontend>docker exec -it Smart-City psql -U ip -d smartcitydb
proto send -d http://127.0.0.1:3000/data -i 5 -v "Hello"
psql (15.8 (Debian 15.8-1.pgdg120+1))
Type "help" for help.

smartcitydb=# CREATE TABLE test (id INTEGER, value VARCHAR(200));