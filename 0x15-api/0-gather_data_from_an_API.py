#!/usr/bin/python3
"""Imports the requests module to handle 
    getting data from an API
    Returns information about an employee's 
    progress given a url
"""
import requests
import sys

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(api_url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [task.get("title") for task in todo if task.get("completed")]
    employee_name = user.get("name")
    total_tasks = len(todo)
    completed_task_count = len(completed_tasks)
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, completed_task_count))

    for completed_task in completed_tasks:
        print("\t {}".format(completed_task))