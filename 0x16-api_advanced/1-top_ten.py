#!/usr/bin/python3

"""Query the top ten hottest posts
Liked for a given subreddit
"""
import requests

def top_ten(subreddit):
    """Working with the pagination function to query the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Linux:0x16.api.advanced:v1.0.0 (by /acceptable/top)"
    }
    params = {
        "Limit": "10"
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    return results.get("posts")