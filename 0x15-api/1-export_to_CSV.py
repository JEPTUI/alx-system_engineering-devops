#!/usr/bin/python3
"""
export data in the CSV format.
"""
import csv
import requests
import sys


def export_to_csv():
    """export data in the CSV format"""
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

    # export data to CSV
    filename = "{}.csv".format(sys.argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = [
                "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": sys.argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    export_to_csv()
