#!/usr/bin/python3
import os
import sys
import requests


def number_of_subscribers(subreddit):
    """Gets information on the numbers of users"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers= {
        
    }