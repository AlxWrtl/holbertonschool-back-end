# API

Background Context:
Traditionally, system administrators relied heavily on Bash scripting for automation tasks. However, with the emergence of Site Reliability Engineers (SREs), who possess broader programming skills, there's a shift towards more efficient languages like Python. This project focuses on utilizing Python to access employee data via an API, organizing it, and exporting it into different data structures.

Resources:

    "Friends don’t let friends program in shell script"
    Understanding APIs: What is an API? What is a REST API?
    Overview of microservices architecture
    Guidelines for clean Python coding: PEP8 Python style

Learning Objectives:
Upon completing this project, you should be able to explain:

    Limitations of Bash scripting
    Concept of APIs and REST APIs
    Microservices architecture
    CSV and JSON formats
    Python coding standards for package, module, class, variable, function, and constant names

Requirements:

    Editors: vi, vim, emacs
    Environment: Ubuntu 20.04 LTS with Python 3.8.x
    Code standards: Follow PEP8 Python style
    Documentation: Include README.md and module documentation
    Error handling: Use get method for dictionary access
    Execution: Use if __name__ == "__main__": to prevent execution on import

Tasks:

0. Gather data from an API

    Write a Python script that retrieves TODO list progress for a given employee ID from a REST API.
    Display employee's progress and completed tasks in a specific format.

1. Export to CSV

    Extend the script from Task 0 to export data in CSV format.
    CSV format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

2. Export to JSON

    Extend the script from Task 0 to export data in JSON format.
    JSON format: {"USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...]}
    File name: USER_ID.json

3. Dictionary of list of dictionaries

    Extend the script from Task 0 to export data for all employees in JSON format.
    JSON format: {"USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ...]}
    File name: todo_all_employees.json

By completing these tasks, you'll gain a deeper understanding of Python scripting, API usage, and data manipulation techniques, essential for modern system administration and SRE roles.