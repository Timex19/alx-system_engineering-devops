#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import csv
import requests
import sys


if __name__ == "__main__":
        url = 'https://jsonplaceholder.typicode.com/'

            userid = sys.argv[1]
                user = '{}users/{}'.format(url, userid)
                    res = requests.get(user)
                        json_o = res.json()
                            name = json_o.get('username')

                                todos = '{}todos?userId={}'.format(url, userid)
                                    res = requests.get(todos)
                                        tasks = res.json()
                                            l_task = []
                                                for task in tasks:
                                                            l_task.append([userid,
