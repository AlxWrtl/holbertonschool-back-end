#!/usr/bin/python3
"""
This script fetches TODO list progress for a given employee from the
JSONPlaceholder API.
It prints the results in a specific format showing completed tasks
and total tasks.
"""

import requests
import sys


def FETCH_EMPLOYEE_TODO_PROGRESS(EMPLOYEE_ID):
    """
    Fetches and prints the TODO list progress for a specific employee.

    Args:
    EMPLOYEE_ID (int): The ID of the employee to query.

    Outputs:
    Prints the progress of employee's TODO tasks in the specified format.
    """
    # Endpoint URLs
    USER_URL = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}"
    TODOS_URL = f"https://jsonplaceholder.typicode.com/todos?userId={
        EMPLOYEE_ID}"

    # Fetch user data
    USER_RESPONSE = requests.get(USER_URL)
    USER_DATA = USER_RESPONSE.json()
    EMPLOYEE_NAME = USER_DATA.get('name')

    # Fetch todos data
    TODOS_RESPONSE = requests.get(TODOS_URL)
    TODOS_DATA = TODOS_RESPONSE.json()

    # Calculate task completion statistics
    TOTAL_TASKS = len(TODOS_DATA)
    COMPLETED_TASKS = [todo for todo in TODOS_DATA if todo.get('completed')]

    # Output the formatted task list
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({
          len(COMPLETED_TASKS)}/{TOTAL_TASKS}):")
    for task in COMPLETED_TASKS:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            EMPLOYEE_ID = int(sys.argv[1])
            FETCH_EMPLOYEE_TODO_PROGRESS(EMPLOYEE_ID)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Please provide an employee ID.")
