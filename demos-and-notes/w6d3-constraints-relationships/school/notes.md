# School Database

## Relationships

### One-to-One
- Less common.
    - Often one-to-one relationships should be enforced at the application level, in the code we write which is making database queries, rather than in the db schema itself. This allows for more flexibility in the database layer.

### One-to-Many
- professors -> class
    - Professors can teach more than one class, a class only has one professor.
- departments -> professors
    - A professor can belong belong to one department, BUT a department has many professors

### Many-to-Many
- courses <-> students
    - A student can have multiple courses, AND a course has multiple students.