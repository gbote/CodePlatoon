# Django Validators

- How to view SQL a migration produces:
python manage.py sqlmigrate twitter_app 0001

## Validator Methods
- Validator functions only need to throw a ValidationError if input is invalid - we don't have to
return `true` for the "happy path

## Using Validation
- We have to manually call our own model validation using the Django model `full_clean` method - the `save` function (example: `MyModel.save()`) does NOT perform model validation. See:
https://docs.djangoproject.com/en/4.0/ref/models/instances/#validating-objects  


## Django Associations

We are going to use Django ORM (Django models) to build relationships between our models and the SQL tables which store their data.
    - Kinds of relationships:
        - One-to-one
            - Less common
            - Usually done w/a foreign key
        - One-to-many
            - Fairly common
            - Often done with a foreign key. Possibly a join table.
        - Many-to-many
            - Fairly common
            - Usually done with a join table

Django ORM is going to do the work of creating the foreign keys & even join tables for us.

- We use the on_delete to say what happens when one model *our* model refers to, like for a foreign key, is deleted. 
    - https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models

- When we use Django ORM to build associations, it will create two-way associations for us, which we can name with the `related_name` argument.

- Django ORM association methods:
    - models.ForeignKey()
        - Use for one-to-many relationships
    - models.OneToField()
        - Use for one-to-one relationships
    - models.ManyToManyField()
        - IMPORTANT: We must also create the model which will be the "join table" manually.
        - Use for many-to-many relationships