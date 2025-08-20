CREATE TABLE IF NOT EXISTS user(
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(50) NOTNULL,
    langSpeak BOOLEAN NOTNULL,
    description TEXT
    




)