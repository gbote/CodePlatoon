import os
import csv
import json

# inventory file creation
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, './assessment2-demo/data/inventory.csv')

inventory_fixture = []
pk_count = 1
with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        video = {}
        video['title'] = row['title']
        video['rating'] = row['rating']
        video['release_year'] = row['release_year']
        video['copies_available'] = row['copies_available']

        fixture = {}
        fixture['model'] = 'video_store_app.video'
        fixture['pk'] = pk_count
        fixture['fields'] = video

        inventory_fixture.append(fixture)
        pk_count += 1


with open("./video_store_project/video_store_app/fixtures/inventory.json", "w") as outfile:
    json.dump(inventory_fixture, outfile)




# customer file creation

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, './assessment2-demo/data/customers.csv')

customers_fixture = []
pk_count = 1
with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        customer = {}
        customer['account_type'] = row['account_type']
        customer['first_name'] = row['first_name']
        customer['last_name'] = row['last_name']

        current_video_rentals = []
        vids = row['current_video_rentals'].split('/')
        for v in vids:
            current_video_rentals.append(v)
        
        customer['current_video_rentals'] = current_video_rentals

        fixture = {}
        fixture['model'] = 'video_store_app.customer'
        fixture['pk'] = pk_count
        fixture['fields'] = customer

        customers_fixture.append(fixture)
        pk_count += 1


with open("./video_store_project/video_store_app/fixtures/customers.json", "w") as outfile:
    json.dump(customers_fixture, outfile)
