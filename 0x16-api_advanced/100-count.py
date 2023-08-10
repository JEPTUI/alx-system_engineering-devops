#!/usr/bin/python3
"""recursive function that queries the Reddit API"""

import requests


def count_words(subreddit, word_list, instances=None, after="", count=0):
    """Parses the title of all hot articles and prints a sorted count
    of given keywords"""
    if instances is None:
        instances = {}

    headers = {'User-Agent': 'CustomUserAgent'}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if word not in instances:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if not instances:
            print("")
            return
        sorted_instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_instances:
            print("{}: {}".format(word, count))
    else:
        count_words(subreddit, word_list, instances, after, count)
