import pytest
import datetime

from tasks import date_fx, change_task


inputs = iter(['22/10/2022', '1/3/245', '29/02/2000'])
invalid_inputs = iter(['54/12/924', '3/14/92', '29/02/2022', 'awoigeha', '13/2', '13.2.24', '1/2/3'])

# Test the date_fx is able to correctly convert input string to four output variables (class, integer, integer, integer)
# Test that the function handles errors, and loops cotinually until a valid date has been entered
class TestDateFx:
    def test_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        assert date_fx(inputs) == (datetime.date(2022, 10, 22), 2022, 10, 22)
        assert date_fx(inputs) == (datetime.date(245, 3, 1), 245, 3, 1)
        assert date_fx(inputs) == (datetime.date(2000, 2, 29), 2000, 2, 29)

    def test_loop_until_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda prompt: next(invalid_inputs))
        assert date_fx(invalid_inputs) == (datetime.date(3, 2, 1), 3, 2, 1)        



    


# https://github.com/flynnwebdev/python-inheritance-lesson/blob/main/exceptions.py

# https://github.com/flynnwebdev/python-inheritance-lesson/blob/main/test_exceptions.py

# https://pypi.org/project/pytest/