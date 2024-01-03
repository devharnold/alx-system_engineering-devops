#!/usr/bin/python3

"""with file 0-gather data
extend this one with exporting to csv
"""
import csv
import sys
import requests

if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    user = user = requests.get(api_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(api_url + "todo", params={"user_id": user_id}).json()

    csv_file_path = "{}.csv".format(user_id)
    with open(csv_file_path, "w", newline="")as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([user_id, username, t.get("completed"), t.get("title")])