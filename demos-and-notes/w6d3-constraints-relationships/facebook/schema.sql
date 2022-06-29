CREATE TABLE user_accounts(
    id serial PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT,
    last_login_date TEXT,
    is_active BOOLEAN
);

CREATE TABLE user_profiles(
    id serial PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES user_accounts (id),
    about_me TEXT,
    password TEXT

);

CREATE TABLE posts(
    id serial PRIMARY KEY,
    user_id INTEGER references user_accounts (id),
    content TEXT
);

CREATE TABLE comments(
    id serial PRIMARY KEY,
    user_id INTEGER references user_accounts (id),
    post_id INTEGER references posts (id),
    content TEXT,
)

-- Think 'Facebook groups' - a user should be able to join multiple groups,
-- a group can contain multiple users.
CREATE TABLE groups(
    id serial PRIMARY KEY,
    name TEXT UNIQUE,
    description TEXT
);

-- a 'join table' or 'through table'
-- common way to model many-to-many relationships
-- like groups.
CREATE TABLE user_group(
    user_id INTEGER REFERENCES user_accounts (id),
    group_id INTEGER REFERENCES groups (id)
); 
