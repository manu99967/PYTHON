CREATE TABLE IF NOT EXISTS parent(
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(250) NOT NULL,
    last_name VARCHAR(250) NOT NULL,
    email VARCHAR(250) UNIQUE NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS parent_address(
    id BIGSERIAL PRIMARY KEY,
    parent_email VARCHAR(250) REFERENCES parent(email) ,
    county_name VARCHAR(250) ,
    town VARCHAR(250),
    longitude REAL,
    latitude REAL,
    house_no VARCHAR(200)
);

INSERT 


