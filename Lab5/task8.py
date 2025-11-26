to_do_list = []

while True:
    action = input("Enter 'add' to add a task, 'view' to see tasks, 'remove' to delete a task, or 'q' to quit: ").lower()
    if action == 'add':
        task = input("Enter a task: ").strip()
        if task:
            to_do_list.append(task)
            print("Task added.")
        else:
            print("Task cannot be empty.")
    elif action == 'view':
        if to_do_list:
            for i, task in enumerate(to_do_list, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the list.")
    elif action == 'remove':
        if to_do_list:
            index = input("Enter the number of the task to remove: ")
            if index.isdigit() and 0 < int(index) <= len(to_do_list):
                to_do_list.pop(int(index) - 1)
                print("Task removed.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to remove.")
    elif action == 'q':
        print("Exiting To-Do List Manager.")
        break
    else:
        print("Invalid action.")
