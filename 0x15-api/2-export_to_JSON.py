#!/usr/bin/python3
''' extension that exports data
    into JSON format
'''
import json
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

    name = user[0].get('name')

    with open('{}.json'.format(_id), 'w') as USER_ID:
        tasks = []
        for task in todo:
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": name
            }
            tasks.append(task_dict)
        data = {_id: tasks}
        json.dump(data, USER_ID)
if __name__ == "__main__":
    if argv[1].isdigit():
        todos(argv[1])
