import datetime

class Task:
    def __init__(self, name, duration, year, month, day):
        self.__name = name
        self.__duration = duration
        self.__due_date = datetime.datetime(year, month, day).date()

    @property
    def values(self):
        return self.__name, self.__duration, self.__due_date.strftime('%d/%m/%Y')

    @property
    def date(self):
        return self.__due_date

    @values.setter
    def values(self, name, duration, year, month, day):
        self.__name = name
        self.__duration = duration
        self.__due_date = datetime.datetime(year, month, day).date()    


def duration_fx(prompt):
    user_input = input(prompt)
    hour, minute = map(int, user_input.split(':'))
    return hour*60 + minute

def date_fx(prompt):
    user_input = input(prompt)
    day, month, year = map(int, user_input.split('/'))
    return year, month, day

# test = Task("laundry", 35, 2000, 10, 3)
# print(test.date)
# print(test.values)
