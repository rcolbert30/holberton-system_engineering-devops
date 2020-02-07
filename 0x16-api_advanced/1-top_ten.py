#!/usr/bin/python3
''' sends query to retieve api data'''

import requests

def top_ten(subreddit):
    url = 'https://api.reddit.com/r/{}/hot?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Hot Post Info'}

    try:
        data = requests.get(url, headers=headers, allow_redirects=False)
        top = reddit_data.json()['data']['children']
        for title in top:
            print(title['data']['title'])

     except BaseException:
         print(None)


if __name__ == '__main__':
    number_of_subscribers(top_ten)
