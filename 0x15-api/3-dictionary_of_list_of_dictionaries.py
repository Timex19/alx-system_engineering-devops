#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
        url = 'https://jsonplaceholder.typicode.com/'
            user = '{}users'.format(url)
                res = requests.get(user)
                    json_o = res.json()
                        d_task = {}
                            for user in json_o:
                                        name = user.get('username')
                                                userid = user.get('id')
                                                        todos = '{}todos?userId={}'.format(url, userid)
                                                                res = requests.get(todos)
                                                                        tasks = res.json()
                                                                                l_task = []
                                                                                        for task in tasks:
                                                                                                        dict_task = {"username": name,
