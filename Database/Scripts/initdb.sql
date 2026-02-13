createdb handshakedb;

DROP TABLE students;
CREATE TABLE students(id SERIAL PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, check_in_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
INSERT INTO students (first_name, last_name) VALUES ('Jim', 'Hawkins');
INSERT INTO students (first_name, last_name) VALUES ('Sally', 'Ride');