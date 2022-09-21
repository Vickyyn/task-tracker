# class Currency:
#     def __init__(self, gold, silver, copper):
#         self.value = (gold, silver, copper)

#     @property
#     def value(self):
#         return self.__gold, self.__silver, self.__copper

#     @value.setter
#     def value(self, value_tuple):
#         gold, silver, copper = value_tuple
#         self.__gold = gold
#         self.__silver = silver
#         self.__copper = copper

#     def add(self, gold, silver, copper):
#         self.__gold += gold
#         self.__silver += silver
#         self.__copper += copper

#     # Define a string representation of the object
#     # Should return a Python expression that reconstructs the object
#     # Intended for use by developers
#     def __repr__(self):
#         return f'Currency(gold={self.__gold}, silver={self.__silver}, copper={self.__copper})'

#     def __str__(self):
#         return f'{self.__gold}G {self.__silver}S {self.__copper}C'


# class Character:
#     __available_races = ['Human', 'Elf', 'Orc', 'Goblin', 'Dwarf']

#     def __init__(self, name, race, *, health=100, attack=10):
#         self.name = name
#         self.race = race
#         self.health = health
#         self.attack = attack
#         self.purse = Currency(0, 0, 0)

#     @classmethod
#     def is_valid_race(cls, race):
#         return race in cls.__available_races

#     def battle(self, other):
#         print(f'{self.name} launches a brutal melee attack on {other.name}!!')


# class Mage(Character):
#     def __init__(self, name, race, *, health=40, attack=50, mana=200):
#         super().__init__(name, race, health=health, attack=attack)
#         self.mana = mana

#     def cast(self, spell):
#         self.mana -= 10

#     def battle(self, other):
#         print(f'{self.name} casts a wicked spell at {other.name}!!')
#         self.cast('fireball')


# class Chest:
#     def __init__(self, items, gold, silver, copper):
#         self.items = items
#         self.cash = Currency(gold, silver, copper)

#     # Transfer contents of this chest to character
#     def loot(self, character):
#         gold, silver, copper = self.cash.value
#         character.purse.add(gold, silver, copper)
#         self.cash.value = (0, 0, 0)


# test = Currency(2, 3, 4)
# print(test)\

# import datetime

# class Task:
#     def __init__(self, name, duration, year, month, day):
#         self.__name = name
#         self.__duration = duration
#         self.__due_date = datetime.datetime(year, month, day).date()

#     @property
#     def values(self):
#         return self.__name, self.__duration, self.__due_date.strftime('%Y-%m-%d')

#     @values.setter
#     def values(self, name, duration, year, month, day):
#         self.__name = name
#         self.__duration = duration
#         self.__due_date = datetime.datetime(year, month, day).date()   

#     @values.setter
#     def values(self, tuple):
#         name, duration, year, month, day = tuple
#         self.__name = name
#         self.__duration = duration
#         self.__due_date = datetime.datetime(year, month, day).date()   


# Test1 = Task('dishes', 35, 2022, 9, 21)
# Test1.values = 'sink', 40, 2022, 9, 21
# Test2 = Test1.values('sink', 40, 2022, 9, 21)
# print(Test1.values)

from tasks import *

# name = input("Name here: ")
# name = Task(name, 5, 3, 2, 1)

# print(name.__dict__)
name1 = Task('shower', 5, 4, 3, 2)
name2 = Task('leggings', 5, 4, 3, 2)
name3 = Task('blanket', 5, 4, 3, 2)
name4 = Task('sleep', 5, 4, 3, 2)
pickle_out = open('tasks.pkl', 'wb')
pickle.dump(name1, pickle_out)
pickle.dump(name2, pickle_out)
pickle.dump(name3, pickle_out)
pickle.dump(name4, pickle_out)
pickle.dump(name1, pickle_out)
pickle_out.close()

list = [name1, name2, name3, name4]
print(list)

write_pickle(None)