#!/usr/bin/python3
''' extension that exports data
    into CSV format
'''
import csv
from sys import argv
from requests import get


def todos(_id):
    ''' function will take in argv1 to return sed ID'''
    user = get("https://jsonplaceholder.typicode.com/users",
               params={'id': _id}).json()
    todo = get("https://jsonplaceholder.typicode.com/todos",
               params={'userId': _id}).json()
    progress = get("https://jsonplaceholder.typicode.com/todos",
                   params={'userId': _id, 'completed': 'true'}).json()

    name = user[0].get('username')
    tasks = len(todo)
    prog = len(progress)

    with open('{}.csv'.format(_id), 'w', encoding='utf-8') as user_file:
        data = csv.writer(user_file, quoting=csv.QUOTE_ALL)

        for task in todo:
                data.writerow([_id, name, task.get('completed'),
                               task.get('title')])


if __name__ == "__main__":
    if argv[1].isdigit():
        todos(argv[1])
