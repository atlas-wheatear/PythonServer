CREATE TABLE words (
    id BIGSERIAL PRIMARY KEY,
    word TEXT UNIQUE,
    inserted TIMESTAMP DEFAULT now()
)
