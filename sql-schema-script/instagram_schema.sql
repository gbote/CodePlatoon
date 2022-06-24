DROP TABLE IF EXISTS profiles CASCADE;
DROP TABLE IF EXISTS users_credentials CASCADE;
DROP TABLE IF EXISTS posts CASCADE;
DROP TABLE IF EXISTS comments CASCADE;
DROP TABLE IF EXISTS follows CASCADE;
DROP TABLE IF EXISTS likes CASCADE;

CREATE TABLE profiles (
  id_pk             SERIAL PRIMARY KEY,
  first_name        varchar(255) NOT NULL,
  last_name         varchar(255) NOT NULL,
  password          varchar(255)
);

CREATE TABLE users_credentials (
  id_pk             SERIAL PRIMARY KEY,
  profile_fk        integer REFERENCES profiles (id_pk),
  username          varchar(255) NOT NULL,
  password          varchar(255) NOT NULL
);

CREATE TABLE posts (
  id_pk             SERIAL PRIMARY KEY,
  author_fk         integer REFERENCES profiles (id_pk),
  content           text
);

CREATE TABLE comments (
  id_pk             SERIAL PRIMARY KEY,
  author_fk         integer REFERENCES profiles (id_pk),
  post_fk           integer REFERENCES posts (id_pk),
  content           text
);

CREATE TABLE follows (
  id_pk             SERIAL PRIMARY KEY,
  follower_fk       integer REFERENCES profiles (id_pk),
  followed_fk       integer REFERENCES profiles (id_pk), 
  CHECK (followed_fk <> follower_fk) --verifies that person can't follow themselves
);

CREATE TABLE likes (
  id_pk             SERIAL PRIMARY KEY,
  liked_by_fk       integer REFERENCES profiles (id_pk),
  liked_post_fk     integer REFERENCES posts (id_pk)
);