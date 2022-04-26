#!/usr/bin/python3
''' queries the Reddit API and prints the titles of the first 10 hot posts '''
import requests


def top_ten(subreddit):
    ''' get top 10 hot posts from given subreddit '''

    base_url = 'http://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'colombiandreamm'}

    res = requests.get(base_url, headers=headers)
    if res.status_code == 200:
        top = res.json()
        for i in range(10):
            print(top['data']['children'][i]['data']['title'])
    else:
        return print('None')
