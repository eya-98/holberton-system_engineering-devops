#!/usr/bin/python3
"""using this REST API, returns information"""
from sys import argv
import requests

if __name__ == "__main__":
    employee_id = argv[1]
    lists = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)).json()
    details = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(employee_id)).json()
    EMPLOYEE_NAME = lists.get('name')
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for i in details:
        TOTAL_NUMBER_OF_TASKS += 1
        if i.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(i.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME,
                  NUMBER_OF_DONE_TASKS,
                  TOTAL_NUMBER_OF_TASKS))
    for TASK in TASK_TITLE:
        print("     {}".format(TASK))
