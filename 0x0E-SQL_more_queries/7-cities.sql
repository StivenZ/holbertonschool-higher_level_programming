-- creates database with foreign key
CREATE DATABASE hbtn_0d_usa IF NOT EXISTS;
USE hbtn_0d_usa;
CREATE TABLE cities IF NOT EXISTS (id INT AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
