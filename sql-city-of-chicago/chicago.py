import psycopg
import csv
from decimal import Decimal

employees_table_creation_query = """
    CREATE TABLE employees (
        id serial PRIMARY KEY, 
        first_name varchar NOT NULL,
        last_name varchar NOT NULL,
        job_title varchar NOT NULL,
        full_or_part_time varchar NOT NULL,
        department varchar NOT NULL,
        annual_salary decimal NOT NULL
    );
"""

def clean_data(csv_row):
    name = csv_row['Name'].split(",")
    first_name = name[1].replace(" ", "", 2)
    first_name = first_name.split(' ')
    cleaned = {'first_name': first_name[0], 'last_name': name[0], 'job_title': csv_row['Job Titles'], 'full_or_part_time': csv_row['Full or Part-Time'], 'department': csv_row['Department']}
    if csv_row['Salary or Hourly'] == 'Hourly':
        salary = Decimal(csv_row['Typical Hours']) * Decimal(csv_row['Hourly Rate']) * 50
    else:
        salary = Decimal(csv_row['Annual Salary'])
    cleaned['annual_salary'] = salary
    return cleaned

connection = psycopg.connect("dbname=chicago_salaries")
connection.execute("DROP TABLE IF EXISTS employees")
connection.execute(employees_table_creation_query)

with open('./salaries.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cleaned_data = clean_data(row)
        connection.execute("INSERT INTO employees (first_name, last_name, job_title, full_or_part_time, department, annual_salary) VALUES (%s, %s, %s, %s, %s, %s)", (cleaned_data['first_name'], cleaned_data['last_name'], cleaned_data['job_title'], cleaned_data['full_or_part_time'], cleaned_data['department'], cleaned_data['annual_salary']))

connection.commit()
connection.close()