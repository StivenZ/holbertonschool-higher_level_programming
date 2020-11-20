-- create a database and a user
CREATE DATABASE hbtn_0d_2 IF NOT EXISTS;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
