tasks = [] #none

#function to add the tasks
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

#function to remove task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print("Unable to find task")

#function to show tasks if available
def show_tasks():
    if tasks:
        print("\n Your tasks:")
        for idx, task in enumerate(tasks,1):
            print(f"{idx}. {task}")
    else:
        print("\n No tasks available")

while True:
    print("\n -- To-Do List App--")
    print("1.Add tasks\n2.Remove tasks\n3.View tasks\n4.Quit")
    choice = input("Choose an option(1-4): ")

    if choice =='1':
        task = input("Enter task: ")
        add_task(task)
    elif choice =='2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice =='4':
        print("Exiting To-Do list!")
        break
    else:
        print("Invalid Choice. Try again")
