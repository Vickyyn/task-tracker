# Task Tracker
## Keep track of your tasks
---

## [Source control repository](https://github.com/Vickyyn/terminal-app)
---

## Style guide: PEP 8
---

## Referenced sources:
### Art 5.7
Haghighi S, 2022, Art 5.7, pypi project, \<https://pypi.org/project/art/\>
### PEP 8
Rossum G, Warsaw B, Coghlan N, 01 Aug 2013, PEP 8 - Style Guide for Python Code, viewed 22 September 2022, \<https://peps.python.org/pep-0008/\>
### PrettyTable 3.4.1
Maurits L, 2022, PrettyTable 3.4.1, \<https://pypi.org/project/prettytable/\>
### Pytest 7.1.3
Krekel H, Oliveira B, Pfannschmidt R, Bruynooghe F, Laugher B, Bruhin F, and others, 2022, pytest 7.1.3, \<https://pypi.org/project/pytest/\>

---

## Features 
### View and sort tasks
- view list all tasks
- sort list by name, amount of time needed to complete task, date to complete task by, or date of original task creation
  
### Add tasks
- add tasks by entering the name, amount of time needed to complete the task, and due date of the task
- ensure no duplicate tasks are created (with the same name)
- confirmation of task creation 

### Edit tasks
- edit a task that has already been created
- able to edit name, time needed, and due date 
- checks there are no duplications with any name changes
- confirmation of details of the task pre and post edit
  
### Delete tasks
- delete a task that has been added
- confirmation prior to deletion of task

### Complete tasks
- complete a task that has been added
- congratulation message with a small surprise
- removal of task from list of tasks

## Project management
[Please see Trello board here.](https://trello.com/b/vgLKMc5B/terminal-app)

## Help documentation 

### Dependencies:
Third party packages used include PrettyTable and Art. Steps for downloading these have been included in the installation instructions below.

### System/hardware requirements: 

### Installation instructions
### First time:
1. Open Terminal
2. Create a virtual environment by running the following command line instruction:
   `python3 -m venv venv`
3. Install the Task Tracker package:
   `python3 -m pip install task-tracker-itsvicky`
4. Install the two dependencies:
   `python3 -m pip install prettytable`
   `python3 -m pip install art`
   `pip install -r requirements.txt`
5. Run the program:

### Subsequent times:
1. Open Terminal
2. Enter the virtual environment created last time:
   `source venv/bin/activate`
3. Run the program: 


including set of instruction which accurately describe how to use and install the application 
NEED TO INSERT HERE 

NOTES:
PEP8: Limit all lines to maximum of 79 characters

cute fonts 'block' 'modular' 'dancingfont' 'funface' 'funfaces'



Other notes:
- 4 or more Python packages into the code
- makes extensive use of functions from one or more Python packages (beyond req of apps)
- 6 or more simple functions and uses at least 5 of these in code 