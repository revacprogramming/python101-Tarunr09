# Databases
# https://www.py4e.com/lessons/database


CREATE TABLE Age (
  name VARCHAR(128),
  age INTEGER 
);
DELETE FROM Age;
INSERT INTO Age (name, age) VALUES ('Alise', 26);
INSERT INTO Age(name, age) VALUES ('Deniss', 30);
INSERT INTO Age (name, age) VALUES ('Kienan', 32);
INSERT INTO Age (name, age) VALUES ('Deano', 40);
SELECT hex(name || age) AS X FROM Age ORDER BY X