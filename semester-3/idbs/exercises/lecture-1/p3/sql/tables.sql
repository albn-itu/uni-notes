SET SCHEMA 'lecture1';

DROP TABLE IF EXISTS dishes CASCADE;
CREATE TABLE dishes (
	id SERIAL PRIMARY KEY,
	name VARCHAR
);

DROP TABLE IF EXISTS available_dishes CASCADE;
CREATE TABLE available_dishes (
	id SERIAL PRIMARY KEY,
	dish_id INT REFERENCES dishes(id),
	amount_sold INT NOT NULL,
	available_from DATE NOT NULL,
	available_to DATE
);

DROP TABLE IF EXISTS suppliers CASCADE;
CREATE TABLE suppliers (
	id SERIAL PRIMARY KEY,
	name VARCHAR
);

DROP TABLE IF EXISTS ingredients CASCADE;
CREATE TABLE ingredients (
	id SERIAL PRIMARY KEY,
	supplier_id INT REFERENCES suppliers(id),
	name VARCHAR
);

DROP TABLE IF EXISTS dish_ingredients CASCADE;
CREATE TABLE dish_ingredients (
	id SERIAL PRIMARY KEY,
	dish_id INT REFERENCES dishes(id),
	ingredient_id INT REFERENCES ingredients(id),
	amount INT NOT NULL
);
