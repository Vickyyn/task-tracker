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
        task_list = read_pickle()

        print(task_list)
        for list in task_list:
            for task in list:
                print(task.values)

    elif main_response.lower() in {"2", "a", "add"}:
        # Create pickle file if it does not already exist
        try:
            with open("tasks.pkl", "x") as file:
                pass 
        except FileExistsError:
            pass 

        # Add tasks
        add_input = True
        while add_input:
            name, duration, due_date, year, month, day = change_task(
                "You are adding a new task! \nWhat is the name of the task? ",
                "Approximately how much time does it take to do the task? Please input in HH:MM format. ",
                "When does the task need to be completed by? Please input in DD/MM/YYYY format. "
            )
            # Create task with the same name 
            name = Task(name, duration, year, month, day)

            # Pickle task
            task_list = read_pickle()
            task_list.append(name)
            write_pickle(task_list)
   
            # Confirm to user that task has been successfully created
            # print(f"\nThe following task has been successfully added! \nName: {name} \nTime needed: {duration} minutes \nComplete by: {datetime.datetime(year, month, day).date()}")
            print(f"\nThe following task has been successfully added! \nName: {task_list[-1].values[0]} \nTime needed: {name.values[1]} minutes \nComplete by (year-month-date): {name.values[2]} \n")

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
        edit_input = True
        while edit_input:

            task_list = read_pickle()

            if not len(task_list):
                print("There are no tasks at the moment! Please add a task first.")
                break

            edit_name = input("Please enter the name of the task you would like to edit: ")            

            for list in task_list:
                for i in list:
                    if i.values[0] == edit_name:
                        print(f"You are editing: \nName: {i.values[0]} \nDuration: {i.values [1]}: \nComplete by (Y-M-D): {i.values[2]} \n")
                        name, duration, due_date, year, month, day = change_task(
                            "What would you like the new name to be? ",
                            "What is the new estimated time to complete the task? Please input in HH:MM format. ",
                            "When is the new completion date? Please input in DD/MM/YYYY format. "
                            )
                        i.values = (name, duration, year, month, day)
                        print(f"\nYou have edited {i.values[0]} to: \nDuration: {i.values[1]} \nComplete by (Y-M-D): {i.values[2]}")
                        break

            write_pickle(task_list)

            # Prompt next step from user
            edit_input = loop_page('edit')
        





    elif main_response.lower() in {"5", "exit"}:
        raise SystemExit


                
   


                




    # elif main_response.lower() in {"4", "c", "complete"}:
    #     # Complete a tasks 
    #     # Reward for completing tasks
    #     pass

