user = 'task'
todolist = []


def showmenu():
    print("Welcome to To do list!:")
    print("1. Add an item:")
    print("2. Delete an item:")
    print("3. View Items:")


while True:
    showmenu()

    def addtasktolist():
        task = input("What is to be done? ")
        todolist.append(task)
        print("Added item:", task)


    def deletetask():
        task = input("Enter a task to delete it ")
        if task in todolist:
            todolist.remove(task)
        else:
            print("Item does not exist in the to-do list ")

    def viewtask():
        print("List of TO-DO Items: ")
        for task in todolist:
            print(task)


    menu = {
        "1": addtasktolist,
        "2": deletetask,
        "3": viewtask,
        }
    choice = input("Enter  Choice: ")
    f = menu.get(choice)
    f()
