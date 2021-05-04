#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    with open("{}.json".format(employee_id), mode='w') as file:
        employees = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(employee_id)).json()
        details = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos"
            .format(employee_id)).json()
        list = []
        for task in details:
            dir = {'task': task.get('title'),
                   'completed': task.get('completed'),
                   'username': employees.get('username')}
            list.append(dir)
        json_file = {employee_id: list}
        json.dump(json_file, file)
