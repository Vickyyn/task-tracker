# More packages in tasks.py
from tasks import *
from art import *
from prettytable import PrettyTable

# Fun title
tprint("Task Tracker", font = 'modular')

# Create pickle file if it does not already exist (the first time program is run)
try:
    with open("tasks.pkl", "x") as file:
        pass 
except FileExistsError:
    pass 

while True:
    # Welcome /  Main Menu
    main_response = input("\nWelcome to Task Tracker! \nToday's date is "
        f"{datetime.datetime.now().date()} \n\nPlease select from options "
        "below: \n 1. View tasks \n 2. Add tasks \n 3. Edit tasks \n 4. "
        "Delete tasks \n 5. Complete tasks \n 6. Exit \n\n")

    # View and sort tasks
    if main_response.lower() in {"1", "v", "view"}:
        view_input = True
        while view_input: 
            # Unpickles data, and if there is no data then prompts user to add data, and exits from this selection
            task_list = read_pickle_msg_if_blank()
            if not task_list:
                break

            # Creates viewing table utilising PrettyTable
            table = PrettyTable()
            table.field_names = ["Name", "Time needed (minutes)", "Complete by"]
            for task in task_list:
                table.add_row([task.values[0], task.values[1], task.values[2]])

            # Print table at entry page for convenience
            print(f"{table}\n\n")

            # View tasks via sorting by different variables
            sort_tasks(table)

            # Prompts user for next action they would like to take, unfortunately cannot use loop page function due to wording
            while True:
                view_input = input("Enter 'view' to return to default view "
                    "page, 'back' to return to main menu, or 'quit' to exit. ")
                if view_input == 'view':
                    print("")
                    break
                if view_input == "back":
                    print("")
                    view_input = False
                    break
                if view_input == "quit":
                    raise SystemExit
                print("Please enter 'view', 'back', or 'quit'")

    # Add tasks
    elif main_response.lower() in {"2", "a", "add"}:
        add_input = True
        while add_input:
            # Create task
            name, duration, due_date, year, month, day = change_task(
                "You are adding a new task! \nWhat is the name of the task? ",
                "Approximately how much time does it take to do the task? "
                    "Please input in HH:MM format. ",
                "When does the task need to be completed by? Please input in "
                    "DD/MM/YYYY format. ")
            named_task = Task(name, duration, year, month, day)

            # Unpickle data
            task_list = read_pickle()

            # Ensure new task name is unique, and subsequent name attempts 
                # are also unique
            while True:
                i = 0
                for task in task_list:
                    i += 1
                    if named_task.values[0] == task.values[0]:
                        named_task.edit_duplicate()
                        i = 0
                if i == len(task_list):
                    break

            # Update and pickle data
            task_list.append(named_task)
            write_pickle(task_list)
   
            # Confirm to user that task has been successfully created
            print("\nThe following task has been successfully added! \nName:"
                f" {task_list[-1].values[0]} \nTime needed (minutes):"
                f" {task_list[-1].values[1]} minutes \nComplete by"
                f" (year-month-date): {task_list[-1].values[2]} \n")

            # Prompt user for next step
            add_input = loop_page('add')
            
    # Edit tasks
    elif main_response.lower() in {"3", "e", "edit"}:
        edit_input = True
        while edit_input:
            # Unpickles data, and if there is no data then prompts user to add data, and exits from this selection
            task_list = read_pickle_msg_if_blank()
            if not task_list:
                break

            # Edit task whilst checking the task exists, and that the new name is unique
            edit_name = input("Please enter the name of the task you would "
                "like to edit: ")  
            name_exists = False
            for i in task_list:
                if i.values[0] == edit_name:
                    name_exists = True
                    # Show details of task to be edited 
                    print(f"You are editing: \nName: {i.values[0]} \n"
                        f"Time needed (minutes): {i.values [1]} \n"
                        f"Complete by (Y-M-D): {i.values[2]} \n")
                    
                    i.edit_self()

                    # Check the name is unique
                    while True:
                        counter = 0
                        for task in task_list:
                            if i.values[0] == task.values[0]:
                                counter += 1
                        if counter == 1:
                            break
                        if counter == 2:
                            i.edit_duplicate()

                    # Confirms edited details and pickles data
                    print(f"\nYou have edited to: \nName: {i.values[0]} \n"
                        f"Time needed (minutes): {i.values[1]} \n"
                        f"Complete by (Y-M-D): {i.values[2]}")
                    write_pickle(task_list)
                    break
            if not name_exists:
                print("This task does not exist. Please try again. \n")

            # Prompt user for next step
            edit_input = loop_page('edit')
        
    # Delete tasks
    elif main_response.lower() in {"4", "d", "delete"}:
        delete_input = True
        while delete_input:
            # Unpickles data, and if there is no data then prompts user to add data, and exits from this selection
            task_list = read_pickle_msg_if_blank()
            if not task_list:
                break

            # Delete task whilst checking the task exists, with confirmation
            delete_name = input("Please enter the name of the task you would "
                "like to delete: ")  
            name_exists = False
            for i in task_list:
                if i.values[0] == delete_name:
                    name_exists = True
                    # Shows details of task and confirms with user whether to delete
                    print(f"You are deleting: \nName: {i.values[0]} \n"
                        f"Time needed (minutes): {i.values [1]}: \n"
                        f"Complete by (Y-M-D): {i.values[2]} \n")
                    while delete_input != 'no':
                        try:
                            delete_input = input("Are you sure you want to "
                                "delete? ")
                            if delete_input.lower() in {"y", "yes"}:
                                # Delete task, print confirmation to user, and pickles data
                                task_list.remove(i)
                                print("Deletion successful \n") 
                                write_pickle(task_list)   
                                delete_input = 'no'
                            elif delete_input.lower() in {"n", "no"}:
                                delete_input = 'no'
                            else:
                                raise ValueError("Please enter 'yes' or 'no'")
                        except ValueError as err:
                            print(err)
            if not name_exists:
                print("This task does not exist. Please try again. \n")

            # Prompt user for next step
            delete_input = loop_page('delete')

    # Complete tasks
    elif main_response.lower() in {"5", "c", "complete"}:
        complete_input = True
        while complete_input:
            # Unpickles data, and if there is no data then prompts user to add data, and exits from this selection
            task_list = read_pickle_msg_if_blank()
            if not task_list:
                break

            # Complete task whilst checking the task exists
            complete_name = input("Please enter the name of the task you "
                "would like to complete: ")  
            name_exists = False          
            for i in task_list:
                if i.values[0] == complete_name:
                    name_exists = True
                    # Confirm task to be completed
                    print(f"You are completing: \nName: {i.values[0]} \n"
                        f"Time needed (minutes): {i.values [1]} \n"
                        f"Complete by (Y-M-D): {i.values[2]} \n")
                    while complete_input != 'no':
                        try:
                            complete_input = input("Is this the right task? ")
                            if complete_input.lower() in {"y", "yes"}:
                                # Complete task with bonus ASCII text art, remove task and pickle data
                                input(f"You have completed the task '{i.values[0]}'!"
                                    " Press enter for a bigger message. ")
                                print("\n\n")
                                tprint("Congratulations", font = "dancingfont")
                                tprint(f"{i.values[0]} has been completed!", font = "rnd-large")
                                print("\n\n")
                                task_list.remove(i)
                                write_pickle(task_list)   
                                complete_input = 'no'
                            elif complete_input.lower() in {"n", "no"}:
                                complete_input = 'no'
                            else:
                                raise ValueError("Please enter 'yes' or 'no' ")
                        except ValueError as err:
                            print(err)
            if not name_exists:
                print("This task does not exist. Please try again. \n")

            # Prompt user for next step
            complete_input = loop_page('complete')            

    # Quit option
    elif main_response.lower() in {"6", "exit"}:
        raise SystemExit
