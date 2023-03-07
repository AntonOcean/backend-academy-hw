INSERT INTO person (name, last_name, balance_max, code, joined_at, balance_min)
VALUES
('Anton324234', 'L', 100, 'rand14234', '2023-10-07 16:57:30', 15),
('Ivan1111223123213', 'M11213', 100, 'rand11113123242343', '2023-10-07 16:57:30', 10) ON CONFLICT DO NOTHING
RETURNING *;
