-- script that creates the database hbtn_0d_usa and the table cities
-- cat 7-cities.sql | mysql -hlocalhost -uroot -p
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
