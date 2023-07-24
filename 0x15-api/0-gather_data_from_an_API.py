#!/usr/bin/python3
"""
Returns employee information about his/her TODO list progress
using the employee ID
"""
import requests
import sys


def display_employee_todo_list():
    """returns API"""
    base_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(base_url)
    
    for u in users.json():
        if u.get('id') == int(sys.argv[1]):
            EMPLOYEE_NAME = (u.get('name'))
            break
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    todos_url = "http://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url)
    for t in todos.json():
        if t.get('userId') == int(sys.argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if t.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(t.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    display_employee_todo_list()
