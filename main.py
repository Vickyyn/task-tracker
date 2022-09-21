# Task Tracker

# Imports including datetime from tasks file
from tasks import *
from art import *
from prettytable import PrettyTable

tprint("Task Tracker", font = 'modular')


while True:
    # Welcome /  Main Menu
    main_response = input("\nWelcome to Task Tracker! \nToday's date is "
    f"{datetime.datetime.now().date()} \n\nPlease select from options below: \n "
    "1. View tasks \n 2. Add tasks \n 3. Edit tasks \n 4. Delete tasks \n "
    "5. Complete tasks \n 6. Exit \n\n")

    if main_response.lower() in {"1", "v", "view"}:
        # View tasks
        # Sort tasks by variables
        view_input = True
        while view_input: 
            task_list = read_if_blank_pickle()
            if not task_list:
                break

            table = PrettyTable()
            table.field_names = ["Name", "Time needed", "Complete by"]
            for task in task_list:
                table.add_row([task.values[0], task.values[1], task.values[2]])

            print(table)
            print("")
            view_input = input(
                "You can view tasks by name, time needed, complete by, or the original creation time of the task prior to any editing. "
                "\nPlease select from the list below: "
                "\n 1. Order by Name \n 2. Order by Time needed \n 3. Order by Complete by date \n 4. Order by creation time (Default) \n")
            if view_input.lower() in {'1', 'name', 'n'}:
                print(table.get_string(sortby = 'Name'))
                print("")
            elif view_input.lower() in {'2', 'time needed', 't'}:
                print(table.get_string(sortby = 'Time needed'))
                print("")
            elif view_input.lower() in {'3', 'complete by', 'c'}:
                print(table.get_string(sortby = 'Complete by'))     
                print("")     
            elif view_input.lower() in {'4', 'd'}:
                print(table)      
                print("")                  

            view_input = loop_page('view')    

        

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
            named_task = Task(name, duration, year, month, day)

            # Pickle task
            task_list = read_pickle()

            while True:
                # Continue looping until only one unique name (as may change to a non-unique name that has already been passed in the first for loop)
                i = 0
                for task in task_list:
                    i += 1
                    if named_task.values[0] == task.values[0]:
                        name, duration, due_date, year, month, day = change_task(
                            "\nA task with this name already exists. \nPlease input a new name: ",
                            "Duration: ",
                            "Complete by (D/M/Y): "
                        )
                        named_task.values = (name, duration, year, month, day)
                        i = 0
                
                if i == len(task_list):
                    break

            task_list.append(named_task)
            write_pickle(task_list)
   
            # Confirm to user that task has been successfully created
            # print(f"\nThe following task has been successfully added! \nName: {name} \nTime needed: {duration} minutes \nComplete by: {datetime.datetime(year, month, day).date()}")
            print(f"\nThe following task has been successfully added! \nName: {task_list[-1].values[0]} \nTime needed: {task_list[-1].values[1]} minutes \nComplete by (year-month-date): {task_list[-1].values[2]} \n")

            # Loop until a correct next step input is received
            add_input = loop_page('add')
            
    elif main_response.lower() in {"3", "e", "edit"}:
        # Edit or delete a task
        edit_input = True
        while edit_input:

            task_list = read_if_blank_pickle()
            if not task_list:
                break

            edit_name = input("Please enter the name of the task you would like to edit: ")  
            name_exists = False
            for i in task_list:
                if i.values[0] == edit_name:
                    name_exists = True
                    print(f"You are editing: \nName: {i.values[0]} \nDuration: {i.values [1]}: \nComplete by (Y-M-D): {i.values[2]} \n")
                    name, duration, due_date, year, month, day = change_task(
                        "What would you like the new name to be? ",
                        "What is the new estimated time to complete the task? Please input in HH:MM format. ",
                        "When is the new completion date? Please input in DD/MM/YYYY format. "
                        )
                    i.values = (name, duration, year, month, day)

                    while True:
                        counter = 0
                        for task in task_list:
                            if i.values[0] == task.values[0]:
                                counter += 1
                        if counter == 1:
                            break
                        if counter == 2:
                            name, duration, due_date, year, month, day = change_task(
                                "\nA task with this name already exists. \nPlease input a new name: ",
                                "Duration: ",
                                "Complete by (D/M/Y): "
                            )
                            i.values = (name, duration, year, month, day)

                    print(f"\nYou have edited to: \nName: {i.values[0]} \nDuration: {i.values[1]} \nComplete by (Y-M-D): {i.values[2]}")
                    write_pickle(task_list)
                    break

            if not name_exists:
                print("This task does not exist. Please try again. \n")

            # Prompt next step from user
            edit_input = loop_page('edit')
        

    elif main_response.lower() in {"4", "d", "delete"}:
     # Delete a task
        delete_input = True
        while delete_input:

            task_list = read_if_blank_pickle()
            if not task_list:
                break

            delete_name = input("Please enter the name of the task you would like to delete: ")  

            name_exists = False
            for i in task_list:
                if i.values[0] == delete_name:
                    name_exists = True
                    print(f"You are deleting: \nName: {i.values[0]} \nDuration: {i.values [1]}: \nComplete by (Y-M-D): {i.values[2]} \n")
                    while delete_input != 'no':
                        try:
                            delete_input = input("Are you sure you want to delete? ")
                            if delete_input.lower() in {"y", "yes"}:
                                task_list.remove(i)
                                print("Deletion successful \n") 
                                delete_input = 'no'
                            elif delete_input.lower() in {"n", "no"}:
                                delete_input = 'no'
                            else:
                                raise ValueError
                        except ValueError:
                            delete_input = input("Please enter 'yes' or 'no' ")
                    write_pickle(task_list)   

            if not name_exists:
                print("This task does not exist. Please try again. \n")

            delete_input = loop_page('delete')

    elif main_response.lower() in {"5", "c", "complete"}:
        complete_input = True
        while complete_input:

            task_list = read_if_blank_pickle()
            if not task_list:
                break

            complete_name = input("Please enter the name of the task you would like to complete: ")            

            for i in task_list:
                if i.values[0] == complete_name:
                    print(f"You are completing: \nName: {i.values[0]} \nDuration: {i.values [1]}: \nComplete by (Y-M-D): {i.values[2]} \n")
                    while complete_input != 'no':
                        try:
                            complete_input = input("Is this the right task? ")
                            if complete_input.lower() in {"y", "yes"}:
                                input(f"You have completed the task '{i.values[0]}'! Press enter for a bigger message.")
                                tprint("Congratulations", font = "dancingfont")
                                tprint(f"{i.values[0]} has been completed!", font = "rnd-large")
                                task_list.remove(i)
                                complete_input = 'no'
                            elif complete_input.lower() in {"n", "no"}:
                                complete_input = 'no'
                            else:
                                raise ValueError
                        except ValueError:
                            complete_input = input("Please enter 'yes' or 'no' ")
                
            write_pickle(task_list)   

            complete_input = loop_page('complete')            




       


    elif main_response.lower() in {"6", "exit"}:
        raise SystemExit


                
   


                




    # elif main_response.lower() in {"4", "c", "complete"}:
    #     # Complete a tasks 
    #     # Reward for completing tasks
    #     pass

