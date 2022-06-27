# Useful Commands

> Before you can run anything related to the database you need to start the server with the command 
    
    > postgres
## In Terminal:
- Create database:  createdb < dbName >
- Psql < dbName >
	
## In PSQL:
- List databases:             \l
- List tables:                \dt
- Describe a table:           \d < tableName >
- Connect to a different DB:  \c < dbName >
- List all commands           \?


---

# Query Examples 

## General query format


    > INSERT into < tablename > (< column_names > ,..) VALUES (< values, ... >)


    > CREATE TABLE <tablename> (<column_name   column_type>,);
    > CREATE DATABASE     <database_name>

    > DROP table <table_name>
         database <database_name>


    > UPDATE table_name
        SET column1 = value1, column2 = value2, ...
        WHERE condition;

    > SELECT <column_names OR *> 
        FROM <table_name> 
        WHERE column_name = ' ' 

    > SELECT <column_names OR *> 
        FROM <table_name>  
        JOIN < table_name> 
        ON column = column 
        WHERE ...

## Class examples:
- Find a student record by name instead of id number

```sql
SELECT * FROM students WHERE last_name = 'Lowe';
```

- List all the students enrolled in a particular course

```sql
SELECT * FROM students LEFT JOIN enrollments ON students.id = student_id WHERE class_id = 4;
```

- Find the number of students who are getting an 'A' in classes they're enrolled in

```sql
select count(*) from students left join enrollments on students.id = student_id where grade = 'A';
```

---

# Benefits of RDBMS:
> Scaling 
- modern dbs allow multiple users to query and update records at the same time and individual database servers can be clustered together to improve that even further

> Data validation
- You can set columns as required 
- data type validation

> Data integrity
- transactions and locking.

> Filtering and searching
- matching certain criteria 
- aggregate functions (sum, average, count, min, max)

---

# Possible applications:

- reading a csv and entering those values into a database using a python script
- loading data into a database using a sql script 
- inserting a new user into the database after they 'sign up' on an application