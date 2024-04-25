-- creates a table users with unique email and name
-- in the database holberton
CREATE DATABASE IF NOT EXISTS holberton;
-- use the database
USE holberton;

-- create the table users
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255));
