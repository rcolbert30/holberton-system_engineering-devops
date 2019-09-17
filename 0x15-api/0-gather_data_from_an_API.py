#!/usr/bin/python3
'''gathers data from an API'''


from requests import get
from sys import argv

url = "https://jsonplaceholder.typicode.com/"


def todo(employ):
    info = get(url + 'users', params={'id': employ}).json()
    data = get(url + 'todos', params={'userId': employ}).json()
    status = get(url + 'todos', params={'userId': employ,
                                        'completed': 'true'}).json()

    name = info[0].get('name')
    tasks = len(data)
    stats = len(status)

    print ("Employee {} is done with tasks({}/{}):".format(name, stats, tasks))

    for i in status:
        print("\t {}".format(i["title"]))

if __name__ == "__main__":
    todo(argv[1])
