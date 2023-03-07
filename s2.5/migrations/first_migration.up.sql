CREATE TABLE IF NOT EXISTS person (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    balance_max INT NOT NULL,
    code TEXT NOT NULL UNIQUE,
    joined_at TIMESTAMP NOT NULL DEFAULT now(),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    balance_min INT NOT NULL CHECK (balance_min >= 0),
    CHECK (balance_min <= balance_max),
    UNIQUE (name, last_name)
);

EXPLAIN ANALYZE SELECT * FROM person WHERE name='d23dfb26-56b2-4f93-83b7-d87a83c974ed' and last_name='d23dfb26-56b2-4f93-83b7-d87a83c974ed';


-- 1 person --> много ... product
-- one to many

CREATE TABLE IF NOT EXISTS product (
    id BIGINT GENERATED ALWAYS AS IDENTITY,
    name TEXT NOT NULL,
    person_id UUID REFERENCES person(id) ON DELETE CASCADE
);


--EXPLAIN ANALYZE SELECT name, last_name, created_at FROM person
--WHERE name='d23dfb26-56b2-4f93-83b7-d87a83c974ed' and
-- last_name='d23dfb26-56b2-4f93-83b7-d87a83c974ed'
--ORDER BY created_at DESC;

--CREATE INDEX IF NOT EXISTS person_name_last_name_created_idx ON person (name, last_name, created_at DESC);


--SELECT
--relname  as table_name,
--pg_size_pretty(pg_total_relation_size(relid)) As "Total Size",
--pg_size_pretty(pg_indexes_size(relid)) as "Index Size",
--pg_size_pretty(pg_relation_size(relid)) as "Actual Size"
--FROM pg_catalog.pg_statio_user_tables
--ORDER BY pg_total_relation_size(relid) DESC;
