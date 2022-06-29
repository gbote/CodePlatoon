-- Enter this in
-- https://app.quickdatabasediagrams.com/
-- You may have to delete this comment


PROFESSORS
------
id serial PK
first_name TEXT
last_name TEXT
department_id FK >- DEPARTMENTS.id

COURSES
---- 
id serial PK
name TEXT
professor_id FK >- PROFESSORS.id

DEPARTMENTS
---
id serial PK
name TEXT

OFFICES
----
id serial PK
address TEXT


OFFICE_PROFESSOR
---
professor_id FK >- PROFESSORS.id
office_id FK >- OFFICES.id