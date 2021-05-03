#!/usr/bin/python3
"""using this REST API, returns information"""
from sys import argv
import requests
import csv

if __name__ == "__main__":
    employee_id = argv[1]
    lists = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)).json()
    details = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(employee_id)).json()
    with open('{}.csv'.format(employee_id), mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL)
        name = lists.get('username')
        for task in details:
            row = [employee_id, name, task.get('completed'), task.get('title')]
            employee_writer.writerow(row)
