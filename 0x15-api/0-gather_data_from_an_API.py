#!/usr/bin/python3

"""
A Script that, uses this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import request
import json
from sys import argv


if __name__ == "__main__":

    sessionReqst = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employe = sessionReqst.get(idURL)
    employeName = sessionReqst.get(nameURL)

    json_reqst = employe.json()
    name = employeName.json()['name']

    totalTasks = 0

    for done_tasks in json_reqst:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
