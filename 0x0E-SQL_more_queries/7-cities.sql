-- creates database with foreign key
CREATE DATABASE hbtn_0d_usa IF NOT EXISTS;
USE hbtn_0d_usa;
CREATE TABLE cities IF NOT EXISTS (id INT AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL FOREIGN KEY REFERENCES hbtn_0d_usa.states(id));
