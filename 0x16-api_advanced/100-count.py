#!/usr/bin/python3
''' api query'''

import requests


def recurse(subreddit, after='', hot_list=[]):
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {'User-Agent': 'Hot Post Recursive Grab Info'}
    x = {'after': after}
    try:
        data = requests.get(url, headers=headers, params=paginate,
                            allow_redirects=False).json()
        articles = reddit_data['data']['children']

        for article in articles:
            _list.append(article['data']['title'])

        n = reddit_data['data']['after']

        if n is None:
            return _list

        return recurse(subreddit, n, _list)

    except BaseException:
        return None
