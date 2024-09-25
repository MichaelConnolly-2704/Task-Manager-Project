task = []

def add_task():
    while True:
        user_input = input("What task would you like to add (enter 'n' to stop): ")
        if user_input.lower() == "n":
            break
        elif user_input.strip():
            task.append({"tasks": user_input, "complete": False})
            print(f"Task '{user_input}' has been added. There are now {len(task)} tasks.")
        else:
            print("Please enter a valid task.")

def mark_complete():
    task_num = int(input("Enter the task number to mark complete: ")) - 1
    if 0 <= task_num < len(task):
        task[task_num]["complete"] = True
        print(f"Task '{task[task_num]['tasks']}' marked as complete.")
    else:
        print("Invalid task number")

def view_tasks():
    if not task:
        print("No tasks available.")
    else:
        for idx, t in enumerate(task, 1):
            status = "Complete" if t["complete"] else "Incomplete"
            print(f"{idx}. {t['tasks']} - {status}")

def delete_task():
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(task):
        removed_task = task.pop(task_num)
        print(f"Task '{removed_task['tasks']}' has been removed.")
    else:
        print("Invalid task number")

def menu():
    while True:
        print("\nMenu:\n1. Add Task\n2. View Tasks\n3. Mark Task as Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

menu()






        
    


