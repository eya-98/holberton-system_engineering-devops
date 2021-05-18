#!/usr/bin/python3
""" a function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    reddit_api = requests.get(url, headers={"User-agent": "Custom"},
                              allow_redirects=False).json()
    try:
        return reddit_api["data"]["subscribers"]
    except Exception:
        return 0
