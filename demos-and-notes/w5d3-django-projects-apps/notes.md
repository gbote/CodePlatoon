# Django Projects and Apps
django apps are divided into modules/apps.
you start with one 'main module', polls_project, that has the same name as the project. this should contain settings and config info
we'll organize our project into one or more apps (polls_app) that contain actual routes and business logic

use the manage.py file to start/stop the app, run migrations, and do other stuff
after creating an app, we must register it in the settings.py

a `view` in django is a function that accepts an HTTP request, and returns an HTTP response. it's called a view because you usually return HTML, so the client has something to look at. 

`~` is an alias for your home folder (the one with your name on it)

## server-side rendering
you have an HTML template, you have data, you need to serve custom HTML with the data interpolated into it.

create a venv: `python -m venv ~/venvs/polls_venv`
activate venv: `source ~/venvs/polls_venv/bin/activate`
install django: `pip install django`
create django project: `python -m django startproject polls_project`
cd into project: `cd polls_project`
create an app: `python manage.py startapp polls_app`


## intermediate templating
### include
    - use include to copy a part of an HTML document into a larger HTML document

### extends
    - use extends to define a layout HTML document that has smaller chunks of HTML inserted into it.