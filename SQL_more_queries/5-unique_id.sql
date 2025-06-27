-- a script that creates the table unique_id on your MySQL server.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256)
);