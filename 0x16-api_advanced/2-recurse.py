#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles
    and If not a valid subreddit, return None."""
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'CustomUserAgent'}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    if after:
        url += f'?after={after}'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if len(posts) > 0:
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)
            after = data['data']['after']
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
