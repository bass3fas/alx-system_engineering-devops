#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    else:
        return 0
