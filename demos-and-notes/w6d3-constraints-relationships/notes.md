# SQL: Constraints & Relationships

## Constraints

### Primary Keys

A unique identifier for a table row

### Foreign Key

Used to form relationships between tables, and if we have table A -> table B
Table A's foreign is Table B's primary key

## Relationships


### One-to-One
- Less common.
    - Often one-to-one relationships should be enforced at the application level, in the code we write which is making database queries, rather than in the db schema itself. This allows for more flexibility in the database layer.

### One-to-Many
- School database
    - Professors can teach more than one class
    - A professor can belong belong to one department, BUT a department has many professors

### Many-to-Many
- School database
    - A student can have multiple courses, AND a course has multiple students