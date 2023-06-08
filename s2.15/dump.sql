CREATE TABLE orders(
   id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   item_id bigint not null,
   status varchar(255) default 'pending',
   created_at timestamp with time zone default now(),
   updated_at timestamp with time zone default now()
);

CREATE TABLE stocks(
   id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   item_id bigint not null,
   count int default 100,
   created_at timestamp with time zone default now(),
   updated_at timestamp with time zone default now()
);

CREATE TABLE deliveries(
   id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   order_id bigint not null,
   created_at timestamp with time zone default now(),
   updated_at timestamp with time zone default now()
);

INSERT INTO stocks(item_id, count) VALUES(1, 100);
INSERT INTO stocks(item_id, count) VALUES(2, 100);
INSERT INTO stocks(item_id, count) VALUES(3, 100);