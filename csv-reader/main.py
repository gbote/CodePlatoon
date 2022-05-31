import csv
animal_type = input("cats or dogs?\n")

try:
    with open(f'./data/{animal_type}.csv') as data:
        reader = csv.DictReader(data)
        for row in reader:
            print(f"{row['name']} is a {row['age']} year old {row['breed']}.")
except Exception:
    print(f"Sorry, we don't have any {animal_type} here.")