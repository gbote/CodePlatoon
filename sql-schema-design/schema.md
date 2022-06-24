# Visualize your schema

Open this file in your text editor and visualize your schema. At the top is your table name. Listed below are all the columns in that table. 

User
-------------------
id
first_name
last_name

Address
-------------------
id
user_id
street 
street2 
city
state
zip_code
country

In the example above, each Address can belong to a User. This is achieved by adding a column called `user_id`, which can match only ONE of the values in the `id` column of the User table. Remember, `id`s are unique; no table can have two `id` values that are the same.

Using the above format, jot down the database for your apps below!

## GrubHub Online Ordering

# Users
--------------------
id              serial int
first_name      varchar(255)
last_name       varchar(255)
phone_number    varchar(15)
address_id      in

# Restaurants
-------------------
id
name
phone_number
address_id

# Menu items
--------------------
id
name
calories
price
restaurant_id

# Addresses
--------------------
id
line_1
line_2
city
state
zip



## Instagram

# user_credentials
-----------------------
id_pk    
profile_id
username
password

# user_profiles
-----------------------
id_pk
first_name
last_name
profile_pic_url

# posts
-----------------------
id_pk
author_fk
content

# comments
-----------------------
id_pk
author_fk
post_fk
content

# follows
-----------------------
id_pk
follower_fk
followed_fk

# likes
-----------------------
id_pk
liked_by_fk
liked_post_fk