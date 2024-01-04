#!/usr/bin/python3
"""Exports task 0 to JSON format"""
import json
import sys
import requests

if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    user = user = requests.get(api_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(api_url + "todo", params={"user_id": user_id}).json()

    with open("{}.json".format(user_id), "w")as jsonfile:
                json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)