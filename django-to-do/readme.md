# Todo List

In this challenge I created a basic CRUD app with just a single record type so that I can focus on practicing the basic actions for CRUD.

I built a basic TODO app that lets us manipulate a list of Todos that they want to complete.

For learning purposes, I'll stick to the seven basic actions I learned:

  ```text
  GET list
  GET show
  GET new
  POST create
  GET edit
  PUT update
  DELETE destroy
  ```

## Release 0: Getting Ready

I started by creating a new virtual environment and then activating it. 

`python -m venv ~/venvs/to-do-env`
`source ~/venvs/to-do-env/bin/activate`

Once I had my virtual environment up and running I told pip to download all the requirements for this app by running `pip install -r requirements.txt`. I had to make sure I was in the main directory of the repo (the one with the readme in it).

Then, I created my project, app, and models to get started!

## Release 1: Create
Since users need a way to get records into the database system, I started with the routes to create new records.

If the user makes a GET request to `/todos/new` they should: 
  * See a form with the required form fields to create a `Todo` object

Submitting the form makes a POST request to `/todos`:
  * It should create the new Todo record in the database. 
  * After the new Todo is created, the user should be redirected to view that Todo.

## Release 2: Read
Next, the users need to read Todo records. Let's start with the `show` action:

A GET request to `/todos/<id>` (where id will be a number corresponding to id of the record you want to view) will:
  * Show the title and description of the Todo 
  * Show a link to edit the existing Todo
  
A GET request to `/todos` should: 
  * Show a list of all Todos that exist
  * Show links to each Todo individually
  * Show a link to create a new Todo
 
## Release 3: Update

Now that users can list records, I built functionality to manipulate those records.

A GET to `/todos/<id>/edit`:
  * Displays a form with the current title and description already filled out in each form field 
  
Submitting the form: 
  * Updates the existing Todo with the new provided values
  * Redirects you back to the show page

## Release 4: Destroy

Finally, I gave users the ability to destroy an existing Todo. (For this project, destroying an existing Todo meant that a certain Todo item was compeleted.)

A POST request to `/todos/<id>/delete`:
  * Deletes the existing Todo
  * Redirects you to the list page
