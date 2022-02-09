SET SCHEMA 'lecture1';

DROP TABLE IF EXISTS manufacturers CASCADE;
CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

DROP TABLE IF EXISTS coffees CASCADE;
CREATE TABLE coffees(
    id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES manufacturers(id),
    name VARCHAR(20)
);

DROP TABLE IF EXISTS coffee_houses CASCADE;
CREATE TABLE coffee_houses (
   id SERIAL PRIMARY KEY,
   name VARCHAR(20),
   license VARCHAR(20)
);

DROP TABLE IF EXISTS sells CASCADE;
CREATE TABLE sells (
   id SERIAL,
   coffee_id INT REFERENCES coffees(id),
   coffeehouse_id INT REFERENCES coffee_houses(id),
   price REAL,
   PRIMARY KEY (id, coffee_id, coffeehouse_id)
);
