# Task Tracker

# Imports
from tasks import *

# Welcome
response = input("Welcome to Task Tracker! \nToday's date is "
f"{datetime.datetime.now().date()} \n\nPlease select from options below: \n "
"1. View tasks \n 2. Add a new task \n 3. Edit or delete a task \n "
"4. Complete a task \n\n")

if response.lower() in {"1", "v", "view"}:
    # View tasks
    # Sort tasks by variables
    print(response.lower())

elif response.lower() in {"2", "a", "add"}:
    name = input("You are adding a new task! \nWhat is the name of the task? ")
    duration = duration_fx("Approximately how much time does it take to do the task? Please input in HH:MM format. ")
    year, month, day = date_fx("When does the task need to be completed by? Please input in DD/MM/YYYY format. ")

    # Create the task
    new_task = Task(name, duration, year, month, day)
    # print(new_task.values)

# elif response.lower() in {"3", "e", "edit", "d", "delete"}:
#     # Edit or delete a task
#     pass

# elif response.lower() in {"4", "c", "complete"}:
#     # Complete a tasks 
#     # Reward for completing tasks
#     pass

