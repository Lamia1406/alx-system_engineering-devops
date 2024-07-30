#!/usr/bin/python3
"""This module returns information about an employee TODO progress
and then export the data in json format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"
    if len(argv) > 1:
        employee = requests.get(
                f'{api}/users/{int(argv[1])}'
                ).json()["username"]
        total_tasks = requests.get(f'{api}/todos?userId={int(argv[1])}').json()
        completed_tasks = [
                task for task in total_tasks
                if task["completed"] is True
                ]

        with open(f'{argv[1]}.json', 'w', newline='') as jsonfile:
            data = {
                    f'{argv[1]}':
                    [{
                        "task": f'{task["title"]}',
                        "completed": task["completed"],
                        "username": f'{employee}'
                        } for task in total_tasks]
                    }
            json.dump(data, jsonfile)
