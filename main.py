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
            with open("tasks.pickle", "ab") as file:
                pickle.dump(name, file)
            # with open("tasks.pkl", "rb") as file:
            #     try: 
            #         task_list = pickle.load(file)
            #     except EOFError:
            #         task_list = []

            # task_list.append(name)

            # with open("tasks.pkl", "wb") as file:
            #     pickle.dump(task_list, file)
            # print(task_list)

            # Confirm to user that task has been successfully created
            # print(f"\nThe following task has been successfully added! \nName: {name} \nTime needed: {duration} minutes \nComplete by: {datetime.datetime(year, month, day).date()}")
            print(f"\nThe following task has been successfully added! \nName: {name.values[0]} \nTime needed: {name.values[1]} minutes \nComplete by (year-month-date): {name.values[2]} \n")

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

        with open ('tasks.pkl', 'rb') as file:
            while True:
                try:
                    a = pickle.load(file)
                except EOFError:
                    print("Nothing with this name was found. Please try again. ")
                    break
                task_list.append(a)
                else:
                    if a.values[0] == edit_name:
                        print(f"You are editing: \nName: {a.values[0]} \nDuration: {a.values [1]}: \nComplete by (Y-M-D): {a.values[2]}")
                        name, duration, due_date, year, month, day = change_task(
                            "What would you like the new name to be? ",
                            "What is the new estimated time to complete the task? Please input in HH:MM format. ",
                            "When is the new completion date? Please input in DD/MM/YYYY format. "
                            )
                        a.values = (name, duration, year, month, day)
                        print(f"You have edited {a.values[0]} to: \nDuration: {a.values[1]} \nComplete by (Y-M-D): {a.values[2]}")
                        break

    elif main_response.lower() in {"5", "exit"}:
        raise SystemExit


                
   


                




    # elif main_response.lower() in {"4", "c", "complete"}:
    #     # Complete a tasks 
    #     # Reward for completing tasks
    #     pass

