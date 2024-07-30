#!/usr/bin/python3
"""This module returns information about an employee TODO progress"""
import requests
from sys import argv

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"
    if len(argv) > 1:
        employee = requests.get(f'{api}/users/{int(argv[1])}').json()["name"]
        total_tasks = requests.get(f'{api}/todos?userId={int(argv[1])}').json()
        completed_tasks = [
                task for task in total_tasks
                if task["completed"] is True
                ]
        print(
                f"Employee {employee_name} is done with tasks("
                f"{len(completed_tasks)}/{len(todos)}):"
                )
        for task in completed_tasks:
            print(f"\t {task['title']}")
