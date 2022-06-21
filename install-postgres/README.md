# Installing Postgres

Before we can insert and query data with postgres, we will need to learn how to install postgres and create our first database. 

There are multiple ways to install postgres. For convenience and consistency, we recommend using `brew` to install postgres.

```sh
brew install postgres
```

This gives us access to several terminal commands that we might use while installing and running postgres (`postgres`, `psql`, `initdb`): `postgres` is used for starting our database server, and `psql` is the database client that we use to connect to our server. Just like you need an http client (e.g. a web browser) to request data from an HTTP server, we need a database client (e.g. `psql`) to request data from the database server. 

## The Data Directory

Next, we need to find or create the data directory for postgres. If you installed postgres with `brew`, the data directory already exists at `/usr/local/var/postgres`. If it doesn't exist yet, you can create it with `initdb`.

```sh
mkdir ~/pgdata
initdb ~/pgdata
```

You can confirm that you found or created the data directory by checking for the postgres config file. If you run `ls /usr/local/var/postgres` (or wherever your data directory is) you should see several files and folders, including the postgres config file, `postgresql.conf`.

Next, we need to tell postgres where the data directory is. There are multiple ways to do this. One way to do this is by setting an environment variable in your startup script (`~/.bash_profile` or `~/.zshrc`).

```sh
export PGDATA=/usr/local/var/postgres
```

## Start the Database Server

Next, we'll start our database. 

```sh
postgres
```

If we didn't specify the data directory with an environment variable, we can specify it here on the command line.

```sh
postgres -D /usr/local/var/postgres/
```

Now, postgres will continue running in this tab until we stop it with `ctrl+c`. If postgres encounters errors while running, those errors will appear here. For now, let's create a new tab in our terminal to continue working. 

## Connect to the Database Server from the client

While the server is running, we can connect to it with our client, `psql`. We want to use `psql` to connect to the database server and create a database, but `psql` requires an existing database to connect to. Fortunately, there's a default database that already exists called `postgres`. We can connect to this database initially, and then create another database. Let's imagine this database stores information about students and teachers for a school, so we'll call the database `school`. 

```sh
psql postgres
create database school;
\q
psql school
```

Your prompt should change to look like this: `school=# `.  If that's what you see in your terminal, then congratulations! You just created and connected to your first postgres database.


## Run Postgres in the background

The way postgres is set up currently, the database server runs in the foreground of a terminal tab. This is very useful while you are learning and debugging, since error messages are immediately visible in the terminal. Some people prefer to run postgres as a background process, so it doesn't permanently occupy a terminal tab. 
If you installed postgres through `brew`, you can run postgres in the background with `brew services start postgres`. This will keep postgres running in the background even if you restart your computer, which can be very convenient. Stop the background service with `brew services stop postgres`.
If you did not use `brew` to install postgres, you can use `pg_ctl start` (postgres control) to start the server, and use `pg_ctl stop` to stop it. Unlike `brew services`, this will NOT keep the server running if you restart your computer. 

## Inspecting background processes

If you run postgres in the background, it's not always obvious if the server is running. One way you can check is with `ps`. By itself, `ps` will show you the processes running in your terminal. For more useful output, `ps -A` will show you all processes from all users. To filter these results, we can _pipe_ the output of `ps -A` into `grep`, a command-line tool for searching through text. 

```sh
ps -A | grep postgres
```

This should show us any line of output from `ps -A` that contains the word 'postgres'. If postgres is running properly in the background, you should see several processes in that list. For example:

```
 3488 ??         0:00.04 /usr/local/Cellar/postgresql/14.0/bin/postgres
 3490 ??         0:00.00 postgres: checkpointer 
 3491 ??         0:00.00 postgres: background writer 
 3492 ??         0:00.00 postgres: walwriter 
 3493 ??         0:00.00 postgres: autovacuum launcher 
 3494 ??         0:00.00 postgres: stats collector 
 3495 ??         0:00.00 postgres: logical replication launcher 
 3497 ttys003    0:00.00 grep postgres
```