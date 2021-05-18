#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        request_API = requests.get(url, allow_redirects=False,
                                   headers={"User-Agent": "Custom"},
                                   params={"limit": 10}).json()
        requesti = request_API["data"]["children"]
        for request in requesti:
            print(request["data"]["title"])
    except Exception:
        print(None)
