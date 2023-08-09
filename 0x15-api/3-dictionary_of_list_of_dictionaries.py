#!/usr/bin/python3
"""
Export all the requested API data to JSON
"""
import json
import requests


def export_all_to_json():
    """return API data"""
    USERS = []
    base_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(base_url)

    for u in users_response.json():
        USERS.append((u.get('id'), u.get('username')))
    TASK_STATUS_TITLE = []
    todos_url = "http://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url)

    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))

    # export to json
    data = dict()
    for u in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == "__main__":
    export_all_to_json()
