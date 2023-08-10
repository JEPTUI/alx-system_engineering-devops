#!/usr/bin/python3
"""recursive function that queries the Reddit API"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, w_counts=None):
    """Parses the title of all hot articles and prints a sorted count of given
    keywords"""
    if w_counts is None:
        w_counts = Counter()
    if after is None:
        after = ""

    headers = {'User-Agent': 'CustomUserAgent'}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    if after:
        url += '?after={}'.format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        results = data['data']['children']
        if len(results) > 0:
            for result in results:
                title = result['data']['title']
                title_lower = title.lower()
                for keyword in word_list:
                    keyword_lower = keyword.lower()
                    if ' {} '.format(keyword_lower) in ' {} '.format(
                            title_lower):
                        w_counts[keyword_lower] += 1
            after = data['data']['after']
            return count_words(subreddit, word_list, after, w_counts)
        else:
            sorted_words = sorted(
                    w_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print('{}: {}'.format(word, count))
    else:
        return
