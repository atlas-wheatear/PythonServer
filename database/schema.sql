CREATE TABLE words (
    id SERIAL PRIMARY KEY,
    word VARCHAR (20) UNIQUE,
    inserted TIMESTAMP DEFAULT current_timestamp
)
