#!/usr/bin/python3
"""
This module returns the number of subscribers of a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers (not active users, total subscribers)
    for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
