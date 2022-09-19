# Task Tracker

# Imports
# import tasks
import datetime

# Welcome
response = input(print("Welcome to Task Tracker! \nToday's date is "
f"{datetime.datetime.now().date()} \n\nPlease select from options below: \n "
"1. View tasks \n 2. Add a new task \n 3. Edit or delete a task \n "
"4. Complete a task"))

try: 
    if response == 1:
        # View tasks
        # Sort tasks by variables
        pass

    elif response == 2:
        name = input(print("You are adding a new task! \n What is the name of the task? "))
        duration = input(print("Approximately how much time does it take to do the task? "))
        due_date = input(print("When does the task need to be completed by? "))
        pass

    elif response == 3:
        # Edit or delete a task
        pass

    elif response == 4:
        # Complete a tasks 
        # Reward for completing tasks
        pass
except ValueError: 
    pass
