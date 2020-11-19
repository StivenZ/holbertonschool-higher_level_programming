-- creates a database with primary key
CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;
CREATE IF NOT EXISTS TABLE states (id INT AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
