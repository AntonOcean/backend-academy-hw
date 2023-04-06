DROP INDEX data_f_l_idx;
CREATE INDEX data_f_l_idx ON data (first_name text_pattern_ops, last_name text_pattern_ops);

DROP INDEX data_f_idx;
DROP INDEX data_l_idx;
CREATE INDEX data_f_idx ON data (first_name text_pattern_ops);
CREATE INDEX data_l_idx ON data (last_name text_pattern_ops);

CREATE INDEX data_i_idx ON data (first_name text_pattern_ops, id);
-- CREATE INDEX data_l_i_idx ON data (last_name text_pattern_ops);

CREATE INDEX data_f_trgm_idx ON data USING GIN (first_name gin_trgm_ops);

DROP INDEX data_t_fts_idx;
CREATE INDEX data_t_fts_idx ON data USING GIN (to_tsvector('russian', text));

CREATE INDEX data_t_trgm_idx ON data USING GIN (text gin_trgm_ops);

EXPLAIN ANALYZE SELECT
    id,
    first_name,
    last_name,
    text
FROM data
WHERE text ilike '%заПЛакать%' or text ilike '%сынок%';

EXPLAIN ANALYZE SELECT
    id,
    first_name,
    last_name,
    text
FROM data
WHERE to_tsvector('russian', text) @@ to_tsquery('russian', 'заПЛакать <-> сынок');

-- Умолять появление теория бочок нервно.
-- Радость болото издали ныне сынок единый горький головка.
-- Постоянный багровый головной естественный редактор о жить заплакать.

-- select to_tsvector('russian', 'анастасия') @@ to_tsquery('russian', 'ан:*');


-- user-data
-- user-sub-data (big)
-- 1 к 1

select to_tsvector('Медицина граница бак очередной табак палец.
Рай сбросить помолчать рот господь. Палка проход сынок инфекция бегать увеличиваться. Пол недостаток угол означать второй деньги.');

select to_tsvector('russian', 'бак граница');
select to_tsquery('russian', 'граница & бак');

select to_tsvector('russian', 'fdkslfdkl dfsdfsdf граница') @@ to_tsquery('russian', 'границы & бак');

select to_tsvector( 'postgraduate' );
select to_tsquery( 'postgres:*' );
SELECT to_tsvector( 'postgraduate' ) @@ to_tsquery( 'postgres' );


select to_tsvector('russian', 'Антон Цитульский');

select to_tsvector('russian', 'Антон Цитульский') @@ to_tsquery('russian', 'а:');

-- CREATE EXTENSION pg_trgm;
-- SELECT * FROM pg_extension;


-- Найти товар в каталоге по описанию

-- pg_trgm - поиск по триграммам - like/ilike
-- fts(to_tsvector, to_tsquery) - поиск по лексеммам - @@
-- text_pattern_ops - поиск по префиксу
