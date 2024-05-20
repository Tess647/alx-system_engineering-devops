#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Base URLs for the API
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Could not retrieve TODOs for user ID {employee_id}.")
        return

    todos_data = todos_response.json()

    # Calculate TODO progress
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py EMPLOYEE_ID")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")

