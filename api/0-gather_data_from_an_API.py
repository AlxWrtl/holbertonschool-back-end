#!/usr/bin/python3
"""
This script fetches TODO list progress for a given employee from the
JSONPlaceholder API.
It prints the results in a specific format showing completed tasks
and total tasks.
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and prints the TODO list progress for a specific employee.

    Args:
    employee_id (int): The ID of the employee to query.

    Outputs:
    Prints the progress of employee's TODO tasks in the specified format.
    """
    # Endpoint URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={
        employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todos data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate task completion statistics
    total_tasks = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo.get('completed')]

    # Output the formatted task list
    print(f"Employee {employee_name} is done with tasks({
          len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Please provide an employee ID.")
