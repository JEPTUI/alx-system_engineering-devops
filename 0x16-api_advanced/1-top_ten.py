#!/usr/bin/python3
"""Querries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed
    and If not a valid subreddit, print None."""
    headers = {'User-Agent': 'CustomUserAgent'}

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if len(posts) > 0:
            print("Top 10 hot posts in /r/{}:".format(subreddit))
            for i, post in enumerate(posts[:10], start=1):
                title = post['data']['title']
                print("{}. {}".format(i, title))
        else:
            print("No hot posts found in /r/{}.".format(subreddit))
    else:
        print(None)
