#!/usr/bin/python3
"""A recursive function that queries the reddit API 
   and returns a list of hot articles for a given subreddit
"""
import requests

def do_recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Linux:0x16.api.advanced:v1.0.0 (by /acceptable/top)"
    }
    params = {
        "after": after,
        "count": count,
        "Limit": "20"
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count = results.get("count")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return do_recurse(subreddit, hot_list, count, after)
    return hot_list