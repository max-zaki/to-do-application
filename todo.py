'''To Do Application'''
# Simple command line interface (CLI)
# Actions:
#   * welcomes users
#   * displays a menu with options to:
#       + add tasks
#       + view tasks
#       + delete tasks
#       + quit application
#   * stores tasks in a list
# Features to use:
#   * input()
#   * error handling:
#       + try
#       + except
#       + else
#       + finally
#       + alert user if:
#           ** they provided invalid input
#           ** there are no tasks to view
#           ** they try to delete a task that doesn't exist
#           ** they select an option on the menu that doesn't exist
#   * functions (for organizing code)
#   * descriptive function names
#   * comments/docstrings
# Testing:
#   * edge cases:
#       + empty lists
#       + invalid input
# README:
#   * gives information about the project
#   * explains how to run and use the project

def greetUser():
    '''Greets the user, prompts for their name, and displays the menu.'''
    name = input("\n\nHi.  Welcome to your To Do App.  What is your name? ")
    print(f"\n\tGreetings, {name}. Please choose from the following menu:\n")
    displayMenu()
    return name

def displayMenu():
    '''Prints a menu with instructions on how to choose the options.'''
    print(f'\n\t\tMENU\n')
    print(f'\t\t================================')
    print(f'\t\tView Tasks\t-----> press "v"')
    print(f'\t\tAdd Task\t-----> press "a"')
    print(f'\t\tDelete Tasks\t-----> press "d"')
    print(f'\t\tQuit Program\t-----> press "q"')
    print(f'\t\t================================\n\n')
    promptUser()
    
def promptUser():
    '''Prompts user for a command.'''
    user_input = input("Enter a command: ")
    processCommands(user_input)

def addTask(task, taskList=[]):
    '''Returns the given task list after appending the given task to it.'''
    if task.strip():
        taskList.append(task)
        print(f'\n\tAdded task "{task}".')
    return taskList

def viewTasks(taskList):
    '''Prints out the given task list if it is not empty.'''
    if taskList != []:
        print('\n\t\t\tTASKS:\n\t\t\t========================')
        for task in taskList:
            print(f"\t\t\t{task}")
        print('\t\t\t========================\n')
    else:
        print("\n\tThere are no tasks to view.")

def deleteTask(taskList, task):
    '''Deletes the specified task from the given taskList, if it exists.'''
    try:
        if task in taskList:
            taskList.remove(task)
            print(f'Deleted "{task}".')
            return taskList
        else:
            print(f'\n\tThe task "{task}" does not exist.')
            return taskList
    except TypeError as e:
        print(f"\n\t\tAn exception has ocurred: {e}")
    
def processCommands(userInput, task_list=[]):
    '''Calls functions based on user input.'''
    if userInput == "v":
        viewTasks(task_list)
    elif userInput == "a":
        new_task = input("\n\t\tEnter a new task: ")
        task_list = addTask(new_task, task_list)
    elif userInput == "d":
        task_to_remove = input("\n\t\tEnter the task you want to delete: ")
        deleteTask(task_list, task_to_remove)
    elif userInput == "q":
        quitProgram()
    else:
        print(f'Your input was not valid. Please choose from the following menu:\n')
    displayMenu()

def quitProgram():
    '''Exits the program.'''
    print(f"\n\nGoodbye!\n\n")
    quit()

tasks = []
name = greetUser()
