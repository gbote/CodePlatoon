# Django ORM

postgreSQL stores data in RELATIONAL tables
Django (and python more generally) store data in objects

a tool that helps translate/map the difference between objects and relational tables is an OBJECT-RELATIONAL MAPPER

when using Django-ORM, we don't write raw SQL anymore, we create classes (Models) from which django creates tables in postgres

another useful feature that django ORM provides is it helps manage changes to our db schema, known as migrations. 

django won't create a database for you, you must connect to an existing database

simply defining a model doesn't immediately change your database. you must create migrations after defining a model, and then run the migrations. 