DROP TABLE IF EXISTS users; 
DROP TABLE IF EXISTS restaurants; 
DROP TABLE IF EXISTS menu_items; 
DROP TABLE IF EXISTS addresses; 

CREATE TABLE addresses (
  id            SERIAL PRIMARY KEY,
  line_1        varchar(255) NOT NULL,
  line_2        varchar(255) NOT NULL,
  city          varchar(255) NOT NULL,
  state         varchar(30) NOT NULL,
  zipcode       varchar(12) NOT NULL
);

CREATE TABLE users (
  id            SERIAL PRIMARY KEY,
  first_name    varchar(255) NOT NULL,
  last_name     varchar(255) NOT NULL,
  phone_number  varchar(15) NOT NULL,
  address_fk    integer REFERENCES addresses (id)
);

CREATE TABLE restaurants (
  id            SERIAL PRIMARY KEY,
  name          varchar(255) NOT NULL,
  phone_number  varchar(15) NOT NULL,
  address_fk    integer REFERENCES addresses (id)
);

CREATE TABLE menu_items (
  id            SERIAL PRIMARY KEY,
  name          varchar(255) NOT NULL,
  calories      integer,
  price         NUMERIC(6, 2) NOT NULL,
  restaurant_fk integer REFERENCES restaurants(id)
);