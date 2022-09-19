from unicodedata import name


class Task:
    def __init__(self, name, duration, due_date):
        self.task = name, duration, due_date

    @property
    def task(self):
        return self.__name, self.__duration, self.__due_date

    @task.setter
    def task(self, name, duration, due_date):
        self.__name = name  

        try:
            self.__duration = duration
        except ValueError:
            print("Duration must be a number")

        try:
            self.__due_date = due_date
        except ValueError:
            print("Please enter in YYYY/MM/DD")

    # @task.deleter
    # def task(self):
    #     response = input((f'Are you sure you want to deleted {self.__name}?'))
    #     if response.upper() == 'YES' or 'Y':

        
    #     print(f'{self.__name} has been deleted!')

class Chore