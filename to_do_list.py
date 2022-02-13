
user = 'task'
todolist = []


def decorator(func):
    def repeat():
        func()
        answer = 'y'
        while answer == input("Do you want to repeat (y/n) ?"):
            if answer == 'y':
                func()

    return repeat


def showmenu():
    print("Welcome to To do list!:")
    print("1. Add an item:")
    print("2. Delete an item:")
    print("3. View Items:")
    print("4. Clear the list:")
    print("5. Find an items:")
    print("6. Mark as done:")
    print("7. View completed tasks: ")
    print("8. Exit: ")


@decorator
def addtasktolist():
    task = input("What is to be done? ")
    todolist.append(task)
    print("Added item:", task)


@decorator
def deletetask():
    task = input("Enter a task to delete it ")
    if task in todolist:
        todolist.remove(task)
    else:
        print("Item does not exist in the to-do list ")


@decorator
def viewtask():
    print("\033[43m  List of TO-DO Items: \033[0m ")                            # выделение желтым цветом
    for task in todolist:
        print(task)


def clearthelist():
    task = input("Do you want to clear the list?(y/n) ")
    if task == 'y':
        todolist.clear()
        print("The list is empty ")
    else:
        showmenu()


@decorator
def findtask():
    print("What do you want to find? ")
    x = input("Enter your word ")
    for i in range(len(todolist)):
        if x in todolist[i]:
            print(todolist[i])


@decorator
def taskscompleted():
    comp = list(map(int, input("Mark as done ").split()))
    for i in comp:
        todolist[i - 1] = todolist[i - 1] + "✔"


@decorator
def allcomp():
    print(" \033[43m Completed tasks: \033[0m  ")                                # выделение желтым цветом
    for i in range(len(todolist)):
        if "✔" in todolist[i]:
            print(todolist[i])


showmenu()


while True:
    menu = {
        "1": addtasktolist,
        "2": deletetask,
        "3": viewtask,
        "4": clearthelist,
        "5": findtask,
        "6": taskscompleted,
        "7": allcomp,

    }
    choice = input("Enter  Choice: ")
    if choice == "8":
        break
    f = menu.get(choice)
    f()
