#!/usr/bin/python3
''' for a given employee id returns info about
    his/her TODO list progress
'''
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
    tasks = len(todo)
    prog = len(progress)

    print("Employee {} is done with tasks({}/{}):".format(name, prog, tasks))

    for task in progress:
        print("\t {}".format(task["title"]))

if __name__ == "__main__":
    if argv[1].isdigit():
        todos(argv[1])
