import pytest
import datetime

# Test the date_fx is able to correctly convert input string to four output variables (class, integer, integer, integer)
# Test that the function handles errors, and loops cotinually until a valid date has been entered
from tasks import date_fx

inputs = iter(['22/10/2022', '1/3/245', '29/02/2000'])
invalid_inputs = iter(['54/12/924', '3/14/92', '29/02/2022', 'awoigeha', '13/2', '13.2.24', '1/2/3'])

class TestDateFx:
    def test_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        assert date_fx(inputs) == (datetime.date(2022, 10, 22), 2022, 10, 22)
        assert date_fx(inputs) == (datetime.date(245, 3, 1), 245, 3, 1)
        assert date_fx(inputs) == (datetime.date(2000, 2, 29), 2000, 2, 29)

    def test_loop_until_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda prompt: next(invalid_inputs))
        assert date_fx(invalid_inputs) == (datetime.date(3, 2, 1), 3, 2, 1)        


# Test edit_self method in class Task is able to update an instance with new attribute values (by using an example instance)
# Test that the method handles incorrect time inputs, and loops continually until valid completion time has been entered
from tasks import Task

test_task = Task('laundry', '1:05', 2022, 9, 30)
new_input = iter(['washing', '0:30', '30/09/2022'])
invalid_time_input = iter(['washing', '0:60', '4:86', 'awgag', '0:0', '1:0', '22/09/2022'])

class TestEditMethod:
    def test_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda prompt: next(new_input))
        test_task.edit_self()
        assert test_task.values[0] == 'washing'
        assert test_task.values[1] == 30
        assert test_task.values[2] == datetime.date(2022, 9, 30)

    def test_loop_until_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda prompt: next(invalid_time_input))
        test_task.edit_self()
        assert test_task.values[0] == 'washing'
        assert test_task.values[1] == 60
        assert test_task.values[2] == datetime.date(2022, 9, 22)        

