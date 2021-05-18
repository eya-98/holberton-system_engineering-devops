#!/usr/bin/python3
"""a recursive function that queries the Reddit
API and returns a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    user_agent = {'User-agent': 'greg'}
    request_API = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                          .format(subreddit, after), headers=user_agent)
    try:
        data = request_API.json().get('data')
        after = data.get('after')
        child = data.get('children')
        for item in child:
            hot_list.append(item['data'].get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    except:
        return(None)
