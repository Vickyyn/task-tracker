# Task Tracker

# Imports including datetime from tasks file
from tasks import *
import pickle

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
            name, duration, due_date, year, month, day = change_task(
                "You are adding a new task! \nWhat is the name of the task? ",
                "Approximately how much time does it take to do the task? Please input in HH:MM format. ",
                "When does the task need to be completed by? Please input in DD/MM/YYYY format. "
            )
            # Create and log the task 
            new_task = Task(name, duration, year, month, day)

            pickle_out = open('tasks.pkl', 'wb')
            pickle.dump(new_task, pickle_out)
            pickle_out.close()
            
            # Confirm to user that task has been successfully created
            # print(f"\nThe following task has been successfully added! \nName: {name} \nTime needed: {duration} minutes \nComplete by: {datetime.datetime(year, month, day).date()}")
            print(f"\nThe following task has been successfully added! \nName: {new_task.values[0]} \nTime needed: {new_task.values[1]} minutes \nComplete by (year-month-date): {new_task.values[2]} \n")

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
        f = open('tasks-list.txt', 'r')
        for row in f.readlines():
            if row.find(edit_name) >=0:
                old_name, old_duration, old_due_date = map(str, row[1:-2].split(', '))
                print("You are now editing the task:")
                print(f'Name: {old_name}')
                print(f'Duration: {old_duration}')
                print(f'Completion date: {old_due_date}')
                # Converting back to an instance (or creating a new one)


                row.replace(str(old_task.values), str(new_task.values))
                break 
        f.close() 


                




    # elif main_response.lower() in {"4", "c", "complete"}:
    #     # Complete a tasks 
    #     # Reward for completing tasks
    #     pass

