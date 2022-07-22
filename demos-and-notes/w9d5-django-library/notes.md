# Library App - Takeaways

## Planning & Implementation
- When you have your code in a "good" (working as expected) state, commit it to git! That way if you have to you can go back to a previous "good" state and not lose too much work.
    - For instance with Django ORM models, we can always create the model and then look at the actual database tables to confirm everything is as we expected.

- Don't be afraid to simply run your code and see what happens! Sometimes the easiest thing to do is run the code & experiment than try to find an answer to your question in online documentation or Stack Overflow.

- If it helps to get some overall context, take some time to diagram or draw out your different models and their relationships before you start coding.

- When coding, try to focus on the smallest unit of work you can do "end-to-end" -- so that you can run your code and confirm everything is working as expected.
    - This helps keep all your code in a good state (i.e. you know it works correctly), and reduces the "surface area" of code you have to check when debugging.

    - The goal is to take a feature or task, and break it into small, independent units of work. This is an "iterative" or "agile" approach.

## Django Models
- One-to-many relationships
    - We define the foreign key on the "many" side of the relationship. 

        - Example: A Reporter can have many Articles, but each Article only has one Reporter. We would define the foreign key in our Article Model class (and have the foreign key reference the Reporter table).

- Many-to-Many relationships
    - We only have to define a many-to-many relationship on one of the models, and Django ORM will take care of the rest!

        - Example: A Book may have multiple Authors, and an Author may have written multiple books. We only need to create a many-to-many relationship field on *either* the Author or Book model, and Django ORM will take care of the rest.
## Fixtures
- Always set the primary key (the `"pk"` field) manually in your fixture files.
    - This will force override any existing data for that model with the same primary key.
        - This is preferred because it is consistent and because it means when you run a fixture it will always have the same result.

        - Otherwise if a model instance already exists with that primary key or this is a model validation issue the fixture data will not get created in the database.

- Start out with a very small amount of sample data when making fixtures until you've fleshed out your model more. This will help with debugging.

- For many-to-many relationships, we do have to create fixtures for each "join table" row we want (to build a relationship).

