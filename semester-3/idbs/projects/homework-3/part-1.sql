-- People
CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    date_of_death DATE DEFAULT NULL
);

-- Member
CREATE TABLE members (
    people_id INTEGER PRIMARY KEY REFERENCES people(id),
    start_date DATE NOT NULL
);

-- Enemy
CREATE TABLE enemies (
    people_id INTEGER PRIMARY KEY REFERENCES people(id)
);

CREATE TABLE opposes (
    member_id INTEGER REFERENCES members(people_id),
    enemy_id INTEGER REFERENCES enemies(people_id),
    start_date DATE NOT NULL,
    end_date DATE DEFAULT NULL,
    PRIMARY KEY(member_id, enemy_id)
);

-- Asset
CREATE TABLE assets (
    name VARCHAR(255) NOT NULL,
    member_id INTEGER REFERENCES members(people_id),
    detail TEXT NOT NULL,
    uses TEXT NOT NULL,
    PRIMARY KEY (name, member_id)
);

-- Linking
CREATE TABLE linkings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    description TEXT NOT NULl
);

-- There is no support for 1..M cardinalities in SQL so just imagine something here
CREATE TABLE participations (
    people_id INTEGER REFERENCES people(id),
    linking_id INTEGER REFERENCES linkings(id),
    PRIMARY KEY (people_id, linking_id)
);

-- Role
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE serve_in (
    member_id INTEGER REFERENCES members(people_id),
    role_id INTEGER REFERENCES roles(id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    salary INTEGER NOT NULL,
    -- Ensure each member can only be appointed to the role once
    PRIMARY KEY (member_id, role_id)
);

-- Party
CREATE TABLE parties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    -- Monitors:
    monitor_member_id INTEGER NOT NULL REFERENCES members(people_id),
    monitor_start_date DATE NOT NULL,
    monitor_end_date DATE NOT NULL
);

-- Sponsor
CREATE TABLE sponsors (
    id SERIAL PRIMARY KEY ,
    name VARCHAR(255),
    address VARCHAR(255),
    industry VARCHAR(255)
);

CREATE TABLE grants (
    sponsor_id INTEGER REFERENCES sponsors(id),
    member_id INTEGER REFERENCES members(people_id),
    date DATE NOT NULL PRIMARY KEY,
    amount INTEGER NOT NULL,
    payback TEXT NOT NULL,

    -- Reviews:
    review_member_id INTEGER REFERENCES members(people_id),
    review_date DATE NOT NULL,
    review_grade DATE NOT NULL
);
