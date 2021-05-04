#!/usr/bin/python3
"""export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    with open('todo_all_employees.json', mode='w') as employement:
        employees = requests.get('https://jsonplaceholder.typicode.com/users/').json()
        details = requests.get('https://jsonplaceholder.typicode.com/users/todos').json()
        for employee in employees:
            ids = employee.get('id')
            todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(ids)).json()
            tasks = []
            for task in todos:
                tasks.append({"username": employee.get("username"),
                              "task": task.get("title"),
                              "completed": task.get("completed")})
            json_file = {ids: tasks}
            json.dump(json_file, employement)

