import datetime

class RangeError(Exception):
    pass


class Task:
    # def __init__(self, name, duration, year, month, day):
    #     self.__name = name
    #     self.__duration = duration
    #     self.__due_date = datetime.datetime(year, month, day).date()

    def __init__(self, name, duration, due_date):
        self.__name = name
        self.__duration = duration
        self.__due_date = due_date

    @property
    def values(self):
        return self.__name, self.__duration, self.__due_date.strftime('%Y/%m/%d')

    @values.setter
    def values(self, name, duration, year, month, day):
        self.__name = name
        self.__duration = duration
        self.__due_date = datetime.datetime(year, month, day).date()    


def duration_fx(prompt):
    hour = None
    minute = None
    while not hour and not minute:
        try:
            user_input = input(prompt)
            hour, minute = map(int, user_input.split(':'))
            if minute >=60:
                raise RangeError("Minutes must be between 0 and 59 inclusive")
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
    while not day and not month and not year:
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
    return due_date


# test = Task("laundry", 35, 2000, 10, 3)
# print(test.date)
# print(test.values)
