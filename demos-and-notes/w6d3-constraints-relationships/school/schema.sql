CREATE TABLE professors (
    id serial PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
    --TODO: Add Department
);

CREATE TABLE courses (
    name TEXT,
    -- ID of professor teaching course
    professor_id integer REFERENCES professors (id)
);

CREATE TABLE departments (
    id serial PRIMARY KEY,
    name TEXT
);

--Add department_id as foreign key to professors table
ALTER TABLE professors
ADD COLUMN department_id integer REFERENCES departments (id);

create TABLE offices (
    id serial PRIMARY KEY,
    building_id INTEGER NOT NULL,
    floor INTEGER NOT NULL,
    office_number INTEGER NOT NULL,

    -- Each professor has their own private office
    -- A professor can have more than one office
    --professor_id INTEGER REFERENCES professors (id)

    -- A professor can only have 1 office
    professor_id INTEGER UNIQUE REFERENCES professors (id)
);
