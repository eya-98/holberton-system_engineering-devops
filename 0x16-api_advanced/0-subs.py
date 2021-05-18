#!/usr/bin/python3
"""Write a function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """return number of subscribers"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    try:
        reddit_api = requests.get(url, headers={"User-Agent": "Custom"},
                                  allow_redirects=False).json()
        return reddit_api["data"]["subscribers"]
    except KeyError:
        return 0
