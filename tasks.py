import datetime
import pickle

class RangeError(Exception):
    pass

class SearchError(Exception):
    pass

class WordValueError(ValueError):
    pass

class Task:
    def __init__(self, name, duration, year, month, day):
        self.__name = name
        self.__duration = duration
        self.__due_date = datetime.datetime(year, month, day).date()

    @property
    def values(self):
        return self.__name, self.__duration, self.__due_date
        # .strftime('%Y-%m-%d')

    @values.setter
    def values(self, value_tuple):
        name, duration, year, month, day = value_tuple
        self.__name = name
        self.__duration = duration
        self.__due_date = datetime.datetime(year, month, day).date()

    def print_confirmation(self, detail):
        print(f"{detail} \n"
            f"Name: {self.__name} \n"
            f"Time needed (minutes): {self.__duration} \n"
            f"Complete by (Y-M-D): {self.__due_date} \n")

    def edit_self(self):
        name, duration, due_date, year, month, day = change_task(
            "What would you like the new name to be? ",
            "What is the new estimated time to complete the task? "
                "Please input in HH:MM format. ",
            "When is the new completion date? "
                "Please input in DD/MM/YYYY format. ")
        self.values = (name, duration, year, month, day)

    def edit_duplicate(self):
        name, duration, due_date, year, month, day = change_task(
            "\nA task with this name already exists. \n"
                "Please input a new name: ",
            "Time needed (HH:MM): ",
            "Complete by (DD/MM/YYYY): ")
        self.values = (name, duration, year, month, day)        

def duration_fx(prompt):
    hour = None
    minute = None
    while not minute:
        try:
            user_input = input(prompt)
            hour, minute = map(int, user_input.split(':'))
            if (hour != 0) and (minute == 0):
                break
            elif minute >=60:
                raise RangeError("Minutes must be between 0 and 59 inclusive")
            elif (hour == 0) and (minute == 0):
                raise RangeError("Tasks must be at least one minute long!")
        except RangeError as err:
            print(err)
            minute = None
        except ValueError:
            print("You must enter two integers, separated by a colon")
    return hour*60 + minute

def date_fx(prompt):
    day = None
    month = None
    year = None
    while not (day and month and year):
        try:
            user_input = input(prompt)
            day, month, year = map(int, user_input.split('/'))
        # Capture user input value errors
        except ValueError:
            print("You must enter three integers separated by /")
            continue

        # Utilising datetime package to see if date is valid
        try:
            due_date = datetime.datetime(year, month, day).date()
        except ValueError as err:
            # Capitalize the error message
            print(str(err).capitalize())
            day = None
            month = None
            year = None
    return due_date, year, month, day

def name_fx(prompt):
    name = input(prompt)
    while not name:
        name = input("Task names cannot be blank! Please input a name: ")
    return name

def change_task(name_prompt, duration_prompt, date_prompt):
    name = name_fx(name_prompt)
    duration = duration_fx(duration_prompt)
    due_date, year, month, day = date_fx(date_prompt)
    return name, duration, due_date, year, month, day

def loop_page(page):
    while True:
        page_input = input(f"Enter '{page.lower()}' to {page.lower()} another"
            " task, 'back' to return to main menu, or 'quit' to exit. ")
        if page_input.lower() == page:
            print("")
            return True
        if page_input.lower() == "back":
            print("")
            return False
        if page_input.lower() == "quit":
            raise SystemExit
        print(f"Please enter '{page}', 'back', or 'quit'")

def read_pickle():
    with open ('tasks.pkl', 'rb') as file:
        try:
            task_list = pickle.load(file)
        except EOFError:
            task_list = []
    return task_list

def read_pickle_msg_if_blank():
    task_list = read_pickle()
    if not task_list:
        input("You have no tasks currently. Please add a task. "
            "Press enter to return.\n")
    return task_list

def write_pickle(task_list):
    with open("tasks.pkl", "wb") as file:
        pickle.dump(task_list, file)

def sort_tasks(table):
    while True:
        try:
            view_input = input(
                "You can order tasks by name, time needed, complete by date, "
                    "or the original creation time of the task prior to any "
                    "editing. \nPlease select from the list below: "
                    "\n 1. Order by Name \n 2. Order by Time needed "
                    "\n 3. Order by Complete by date "
                    "\n 4. Order by creation time (Default) \n")
            if view_input.lower() in {'1', 'name', 'n'}:
                print(table.get_string(sortby = 'Name'))
                print("")
                break
            elif view_input.lower() in {'2', 'time needed', 't'}:
                print(table.get_string(sortby = 'Time needed (minutes)'))
                print("")
                break
            elif view_input.lower() in {'3', 'complete by', 'c'}:
                print(table.get_string(sortby = 'Complete by'))     
                print("")
                break     
            elif view_input.lower() in {'4', 'd'}:
                print(table)      
                print("")
                break
            else:
                raise ValueError("\nNOTE: Please input '1', '2', '3', "
                    "or '4'! \n")                  
        except ValueError as err:
            print(err) 

