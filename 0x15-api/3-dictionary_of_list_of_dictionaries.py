#!/usr/bin/python3
''' extension that exports data
    into JSON format
'''
import json
from sys import argv
from requests import get


def todos():
    ''' function will take in argv1 to return sed ID'''
    user = get("https://jsonplaceholder.typicode.com/users").json()
    todo = get("https://jsonplaceholder.typicode.com/todos").json()
    progress = get("https://jsonplaceholder.typicode.com/todos").json()

    with open("todo_all_employees.json", 'w') as new_file:

        tasks_dict = {}

        for user in todo:
            emp_tasks = []
            username = user.get('username')
            user_id = user.get('id')

            for task in progress:
                if task.get('userId') == user_id:
                    task_dict = {
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": username
                        }
                    emp_tasks.append(task_dict)
                tasks_dict.update({user_id: emp_tasks})
        json.dump(tasks_dict, new_file)

if __name__ == "__main__":
    todos()
