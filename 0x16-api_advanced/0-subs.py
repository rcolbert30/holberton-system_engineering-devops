#!/usr/bin/python3
''' sends query to apit to retrieve data '''

import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'subscriber info'}

    try:
        data = requests.get(url, headers=headers, allow_redirects=False)
        subs = reddit_data.json()['data']['subscribers']
        return (subs)

    except BaseException:
        return 0

if __name__ == '__main__':
    number_of_subscribers(subreddit)
