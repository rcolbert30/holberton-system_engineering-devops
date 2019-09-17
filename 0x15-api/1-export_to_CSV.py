#!/usr/bin/python3
'''gets data from an API, exports to csv'''
import csv
from requests import get
from sys import argv

url = "https://jsonplaceholder.typicode.com/"


def todo_csv(employ):
    info = get(url + 'users', params={'id': employ}).json()
    data = get(url + 'todos', params={'userId': employ}).json()
    name = info[0].get('username')

    with open('{}.csv'.format(employ), 'w', newline='', encoding='utf-8') as x:
        deets = csv.writer(x, quoting=csv.QUOTE_ALL)

        for i in data:
            deets.writerow([employ, name,  i.get('completed'), i.get('title')])


if __name__ == "__main__":
    todo_csv(argv[1])
