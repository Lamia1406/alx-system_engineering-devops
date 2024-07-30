#!/usr/bin/python3
"""This module returns information about an employee TODO progress
and then export the data in csv format"""
import csv
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

        with open(f'{argv[1]}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            for task in total_tasks:
                writer.writerow([argv[1],
                                employee,
                                task["completed"],
                                task["title"]]
                                )
