# Task Tracker
Keep track of your tasks!

--- 

## [Source control repository](https://github.com/Vickyyn/task-tracker)

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

---

## Style guide: 
PEP 8

---

## Referenced sources:
### Art 5.7
Haghighi S, 2022, Art 5.7, pypi project, \<https://pypi.org/project/art/>
### PEP 8
Rossum G, Warsaw B, Coghlan N, 01 Aug 2013, PEP 8 - Style Guide for Python Code, viewed 22 September 2022, \<https://peps.python.org/pep-0008/>
### PrettyTable 3.4.1
Maurits L, 2022, PrettyTable 3.4.1, \<https://pypi.org/project/prettytable/\>
### Pytest 7.1.3
Krekel H, Oliveira B, Pfannschmidt R, Bruynooghe F, Laugher B, Bruhin F, and others, 2022, pytest 7.1.3, \<https://pypi.org/project/pytest/>

---

## Project management
[Please see Trello board here.](https://trello.com/b/vgLKMc5B/terminal-app)

---

## Help documentation 

### System/hardware requirements: 
Python 3 (please see https://www.python.org/downloads/ to download if needed)  

### Dependencies:
Third party packages used include PrettyTable 3.4.1 and Art 5.7, as well as a subdependency of wcwidth 0.2.5. These are automatically installed (if not already installed) by following the below installation guide.

### Installation and usage instructions
1. Open Terminal
2. Clone (or download) the files for the application by running the following (you only have to do this once - skip this step when running the application on subsequent times):  
   `git clone git@github.com:Vickyyn/task-tracker.git`  
   Note: If you cannot do this step due to not having git installed, please follow this guide for installation: https://github.com/git-guides/install-git
3. Run the following command to start the application! It will let you know if there are any errors prior to running the application:     
   `./src/run_task_tracker.sh`
