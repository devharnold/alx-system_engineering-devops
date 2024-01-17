#!/usr/bin/python3
"""A recursive function that queries the reddit API 
   and returns a list of hot articles for a given subreddit
"""
import requests

def do_recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Linux:0x16.api.advanced:v1.0.0 (by /acceptable/top)"
    }
    params = {
        "Limit": "20"
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    response_json = response.json()
    paginated = [response_json]

    while next in response.links:
        response = requests.get(response.links['next']['url'], headers=headers)
        paginated.append(response.json())
    print(paginated)