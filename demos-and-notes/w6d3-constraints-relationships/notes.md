# SQL: Constraints & Relationships

## Constraints

Primary Keys and Foreign Keys are the most important table constraints. Other constraints we can apply to columns are `UNIQUE`, `NOT NULL`, and so on. Each is important and has its role. [Check out the PostGRES docs on constraints - they are very friendly](https://www.postgresql.org/docs/current/ddl-constraints.html)

### Primary Keys
A unique identifier for a table row

### Foreign Key
Used to form relationships between tables, and if we have table A -> table B, table A's foreign key is Table B's primary key. 

## Relationships

Using SQL to specify relationships between tables in our database is a critical part of good database design. These are the core relationships in relational databases.


### One-to-One
This is less common. Often one-to-one relationships should be enforced at the application level, in the code we write which is making database queries, rather than in the db schema itself. This allows for more flexibility in the database layer.

In the school database, a professor may only have one office. In the facebook database, a `user_account` can only be associated with one `user_profile` and vice versa.

### One-to-Many
For example - a user may have many comments. Look in the notes files of the facebook and school directories here for more examples : ).

### Many-to-Many
This should commonly be implemented using a 'join table. Look in the facebook database schema at the `user_group` join table to see how
many-to-many relationships are handled.