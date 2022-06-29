-- Enter this in
-- https://app.quickdatabasediagrams.com/
-- You may have to delete this comment


USER_ACCOUNTS
---
id serial PK
username UNIQUE TEXT
email UNIQUE TEXT
password TEXT
last_login_date TEXT
is_active BOOLEAN


USER_PROFILES
----
id serial PK 
user_id UNIQUE FK >- USER_ACCOUNTS.id
profile_photo_url TEXT
about_me TEXT


POSTS
---
id serial PK
content TEXT
user_id FK >- USER_ACCOUNTS.id


COMMENTS
----
id serial PK
content TEXT
user_id NOT NULL FK >- USER_ACCOUNTS.id
post_id NOT NULL FK >- POSTS.id

GROUPS
----
id serial PK
name UNIQUE TEXT
description TEXT

USER_GROUP
----
user_id FK >- USER_ACCOUNTS.id
group_id FK >- GROUPS.id