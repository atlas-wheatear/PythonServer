DROP TABLE IF EXISTS Words

CREATE TABLE Words (
    id SERIAL PRIMARY KEY,
    word VARCHAR (20) UNIQUE,
    inserted DATETIME DEFAULT current_timestamp
)