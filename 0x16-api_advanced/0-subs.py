#!/usr/bin/python3
"""Querries the Reddit API and returns the number of subscribers
for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit
    and if an invalid subreddit is given, the function returns 0"""
    headers = {'User-Agent': 'CustomUserAgent'}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Send a GET request to API endpoin
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        return 0
    else:
        return 0
