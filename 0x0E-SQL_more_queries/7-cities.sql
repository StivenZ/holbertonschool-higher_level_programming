-- creates database with foreign key
CREATE DATABASE hbtn_0d_usa IF NOT EXISTS;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL);
