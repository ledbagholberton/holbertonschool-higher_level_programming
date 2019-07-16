-- create a table unique_id
-- database name come in args fron CLI
CREATE TABLE IF NOT EXISTS unique_id (id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR(256));
