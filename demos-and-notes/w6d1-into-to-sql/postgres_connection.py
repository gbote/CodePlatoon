import psycopg

# Connect to an existing database
with psycopg.connect(dbname='test', user='postgres', password='postgres', host='localhost', port= '5432') as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cursor:

        # Execute a command: this creates a new table

        cursor.execute("""
            DROP TABLE IF EXISTS TEST;
            
            CREATE TABLE test (
                id serial PRIMARY KEY,
                num integer,
                data text);
            """)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cursor.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s);",
            (100, "abc'def"))

        conn.commit()

        # Query the database and obtain data as Python objects.
        cursor.execute("SELECT * FROM test;")
        cursor.fetchone()
        # will return (1, 100, "abc'def")

        # You can use `cursor.fetchmany()`, `cursor.fetchall()` to return a list
        # of several records, or even iterate on the sorsor
        for record in cursor:
            print(record)

        # Make the changes to the database persistent
        #conn.commit()


