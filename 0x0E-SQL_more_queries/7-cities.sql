-- creates database and table
-- create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- create table cities with foreign key
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id),
       name VARCHAR(256) NOT NULL);
