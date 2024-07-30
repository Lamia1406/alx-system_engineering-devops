#!/usr/bin/python3
"""This module returns information about all employees TODO progress
and then export the data in json format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"
    employees = requests.get(
            f'{api}/users?username, id'
            ).json()
    all_tasks = requests.get(f'{api}/todos').json()

    with open(f'todo_all_employees.json', 'w', newline='') as jsonfile:
        data = {
                employee["id"]: [{
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee["username"]
                    } for task in all_tasks
                        if task["userId"] == employee["id"]
                        ]
                for employee in employees
                }
        json.dump(data, jsonfile)
