# Django-ORM


## Topics Covered / Goals
- Be able to create a new Django project within your virtual enviornment
- Understand how to create a database and models
- Know how to communicate with your database using Python and Django ORM

## Lesson

- [Django ORM Slides](../page-resources/Intro_Django_ORM.pdf)

**Connecting Django to Postgresql using Django ORM**

Soon, we are going to begin using Django, a Python framework, to develop our web applications. You don't need to know the in's and out's of Django right now; we're just going to be using the *Django ORM*. *ORM* stands for *Object Relational Mapping* and it's a way for us to use Python code to talk to a database. Instead of writing raw SQL statements, we write Python code using Django ORM syntax to perform SQL queries. It's very important to note that there is no magic here - you type Django ORM code, the interpreter will translate it to SQL, and it'll pass that SQL to the database. Once a result comes back from the database (in raw SQL), the interpreter will translate it back to Django ORM code and pass it back to you.



**Starting a New Django Project**

Once we have our venv up and running, we can install Django and start a new project. We are going to call our project name `school`, but you can call it whatever you want.

```bash
$ pip install django
$ django-admin startproject <projectname>
$ cd <projectname>
```

**Create a database**

Today we're learning on how the Python classes we write will connect to our database using Django ORM. We'll be creating a `school` database with one table: `students`.

```bash
$ createdb school
```

**Pyscopg2**

Now we install the Python library that will help Django talk to Postgres.

```bash
$ pip install psycopg2
```

And then tell Django we want to use Postgres as our database instead of the default SQL adapter, SQLite3. We also tell it what database to attach to

```python
## school/settings.py
## our settings.py file is in the school directory, but if you named your app a different name then it look for that folder name.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'school',
    }
}
```

**Create our App**

Django projects are split into many apps (i.e., a project has many apps). Imagine a new _project_ at Amazon where they are selling lots of space on the Moon. That _project_ requires a bunch of different _apps_ in order to run. For example, there might be a billing _app_ to collect money from individuals, a searching _app_ for people to look up lots, a VIP _app_ where they target VIPs, etc. Today, our `school` project will just start with a `students` app.

```bash
$ python manage.py startapp attendance
```

Next, we need to add the `attendance` app to our `settings.py` file in our school folder.
```python
## school/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'attendance',
]
```

**Creating Our Model**

Now we can create our `student` model:

```python
## attendance/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
```

We've created a Python class that directly correlates to a database table (i.e., a model). Next, let's tell Django to create the necessary code for us to get this table into the database:

```bash
$ python manage.py makemigrations attendance
```

A folder was just generated called `migrations`. Look inside there and take a look at the Django code that was generated for us to put our tables into the database. Next, let's `migrate` our data from the app into the database itself:

```bash
$ python manage.py migrate
```

We should have a `attendance_student` students table in our db. Check it out with `psql school`

**Django Console**

While we can interact with our data using Postgres, more often we want to interact with our data using Python. We're going to use a console for our project that will pull in all our Python classes and allow us to query the database directly using Django's ORM.

```bash
$ python manage.py shell
from school.models import Student
```

The shell will load in all of our models and libraries from Django. Once in the shell, we can create a new student.

```bash
In [1]: student = Student(name="Jon", email="jon@jon.com")
In [2]: student.save()
```

We're starting to see things come together - the object oriented lessons from weeks 2 and 3 were in preparation for this. Just by writing those two lines of code, we are able to instantiate a Student object for us and save it into the database. Under the hood, it's just running:

```sql
INSERT into students (name, email) VALUES ('Jon', 'jon@jon.com')
```

Now we can query our database using Python and see our new record.
```bash
In [3]: Student.objects.all()
## SELECT * from students;
```
You should get back a query object. Exit the shell by typing `exit`. Let's confirm that our new record got saved in our Postgres db.

```bash
$ psql school
psql (11.1, server 9.6.3)
Type "help" for help.

school= \d
                          List of relations
 Schema |               Name                |   Type   |     Owner
--------+-----------------------------------+----------+---------------
 public | attendance_student                | table    | joshuaalletto
 public | attendance_student_id_seq         | sequence | joshuaalletto
 public | auth_group                        | table    | joshuaalletto
 ...

```
Django creates our database tables with the project name first, followed by the app name. So `attendance_student` is what we are looking for. Let's query for the records in that table and see what we get.

```bash
## select * from attendance_student;
school=
 id | name | email
----+------+-----+
  1 | Jon | jon@jon.com
(1 row)
```

**Conclusion**

We've created a database using Postgres and connected it to a Django project within a virtual environment. Then, we created an app within that project, created a model that links directly to a table in our database, and migrated over its columns from Django to Postgres.

Next, we created a record (row) in our database using just Python and verified that it entered our Postgres database. Today, we're going to be learning just how powerful Django ORM is and the types of complicated SQL queries we can write in just a few lines of Python.

## External Resources
- [Django Docs](https://docs.djangoproject.com/en/2.2/)
- [Django Queries Cheat Sheet](https://github.com/chrisdl/Django-QuerySet-Cheatsheet)
- [Django Validators Resource](https://docs.djangoproject.com/en/2.2/ref/validators/)
- [Database Diagramer](https://www.quickdatabasediagrams.com/)

## Assignments
- [Django Queries](https://github.com/romeoplatoon/django-queries)



