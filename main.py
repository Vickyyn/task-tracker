# Task Tracker

# Imports
from tasks import *

while True:
    # Welcome /  Main Menu
    main_response = input("Welcome to Task Tracker! \nToday's date is "
    f"{datetime.datetime.now().date()} \n\nPlease select from options below: \n "
    "1. View tasks \n 2. Add a new task \n 3. Edit or delete a task \n "
    "4. Complete a task \n 5. Exit \n\n")

    if main_response.lower() in {"1", "v", "view"}:
        # View tasks
        # Sort tasks by variables
        print(main_response.lower())

    elif main_response.lower() in {"2", "a", "add"}:
        # Add tasks
        add_input = True
        while add_input:
            name = input("You are adding a new task! \nWhat is the name of the task? ")
            duration = duration_fx("Approximately how much time does it take to do the task? Please input in HH:MM format. ")
            due_date = date_fx("When does the task need to be completed by? Please input in DD/MM/YYYY format. ")

            # Create and log the task 
            new_task = Task(name, duration, due_date)
            f = open('tasks-list.txt', 'a')
            f.write(f"{str(new_task.values)}\n")
            f.close()

            # Confirm to user that task has been successfully created
            # print(f"\nThe following task has been successfully added! \nName: {name} \nTime needed: {duration} minutes \nComplete by: {datetime.datetime(year, month, day).date()}")
            print(f"\nThe following task has been successfully added! \nName: {new_task.values[0]} \nTime needed: {new_task.values[1]} minutes \nComplete by (year/month/date): {new_task.values[2]} \n")

            # Loop until a correct next step input is received
            while True:
                add_input = input("Enter 'add' to add another task, 'back' to return to main menu, or 'quit' to exit. ")
                if add_input.lower() == "add":
                    print("")
                    break
                if add_input.lower() == "back":
                    print("")
                    add_input = False
                    break
                if add_input.lower() == "quit":
                    raise SystemExit
                print("Please enter 'add', 'back', or 'quit'")
            
    elif main_response.lower() in {"3", "e", "edit", "d", "delete"}:
        # Edit or delete a task
        # Edit
        edit_name = input("Please enter the name of the task you would like to edit: ")
        f = open('tasks-list.txt', 'a')
        for row in f.readlines():
            if row.find(edit_name) == 0:
                original_task = Task(row)
                name = input("What would you like the new name to be? ")
                duration = duration_fx("What is the new estimated time to complete the task? Please input in HH:MM format. ")
                due_date = date_fx("When is the new completion date? Please input in DD/MM/YYYY format. ")
                new_task = original_task.values(name, duration, due_date)
                




    # elif main_response.lower() in {"4", "c", "complete"}:
    #     # Complete a tasks 
    #     # Reward for completing tasks
    #     pass

