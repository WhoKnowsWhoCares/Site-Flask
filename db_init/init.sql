-- CREATE TABLE quote (
--     id SERIAL PRIMARY KEY,
--     quote character varying(255) NOT NULL UNIQUE,
--     author character varying(255) NOT NULL,
--     created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- INSERT INTO quote (id, quote, author) VALUES 
-- (1, 'There are only two kinds of languages: the ones people complain about and the ones nobody uses.', 'Bjarne Stroustrup');