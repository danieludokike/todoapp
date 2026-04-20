from database import *

# create table function called
create_table() # call the create table, to ensure our table get created

def display_tasks(tasks):
    print("\n{:<5} {:<15} {:<10}".format("ID", "TITLE", "STATUS"))
    print("-" * 35)
    
    for task in tasks:
        task_id, title, completed = task
        status = "Done" if completed else "Pending"
        print("{:<5} {:<15} {:<10}".format(task_id, title, status))


while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        title = input("Enter task: ")
        add_task(title)
        
    elif choice == "2":
        tasks = get_tasks()
        display_tasks(tasks)
            
    elif choice == "3":
        task_id = int(input("Task ID: "))
        complete_task(task_id)
        
    elif choice == "4":
        task_id = int(input("Task ID: "))
        delete_task(task_id)
        
    elif choice == "5":
        break