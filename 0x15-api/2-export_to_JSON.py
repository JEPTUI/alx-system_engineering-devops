#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to
export data in the JSON format.import argv
"""
import json
import requests
import sys


def export_to_json():
    """return API"""
    base_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(base_url)

    for u in users.json():
        if u.get('id') == int(sys.argv[1]):
            USERNAME = (u.get('username'))
            break
    TASK_STATUS_TITLE = []
    todos_url = "http://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url)

    for t in todos.json():
        if t.get('userId') == int(sys.argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    # export to json
    t = []
    for task in TASK_STATUS_TITLE:
        t.append({"task": task[1], "completed": task[0], "username": USERNAME})
    data = {str(sys.argv[1]): t}
    filename = "{}.json".format(sys.argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    export_to_json()
