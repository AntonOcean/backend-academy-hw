DESCRIBE CLUSTER;


CREATE KEYSPACE hotel WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};


CREATE TABLE hotels_by_poi (
     poi_id int,
     hotel_id text,
     name text,
     phone text,
     address text,
     PRIMARY KEY ((poi_id), hotel_id) )
WITH CLUSTERING ORDER BY (hotel_id ASC);

CREATE TABLE hotels (
    id text PRIMARY KEY,
    name text,
    phone text,
    address text);

INSERT INTO hotels (id, name, phone, address)
VALUES ('my-first-hotel', 'name', '8901', 'moscow');

INSERT INTO hotels_by_poi (poi_id, hotel_id, name, phone, address)
VALUES (12, 'my-hotel', 'name 1', '8901', 'moscow');

INSERT INTO hotels_by_poi (poi_id, hotel_id, name, phone, address)
VALUES (13, 'my-hotel-1', 'name 1 1', '89012', 'moscow2');

TRACING ON;

SELECT * FROM hotels;

SELECT * FROM hotels_by_poi WHERE poi_id = 12 AND address = 'moscow' ALLOW FILTERING;