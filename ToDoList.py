tasks = []

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({
        'title': title,
        'description': description,
        'due_date': due_date,
        'completed': False
    })
    print("Task added successfully!")

def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("------ TO-DO LIST ------")
        for index, task in enumerate(tasks, start=1):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{index}. {task['title']} - {task['description']} - Due: {task['due_date']} [{status}]")
        print("------------------------")

def edit_task(index):
    if 1 <= index <= len(tasks):
        task = tasks[index - 1]
        print("Current task details:")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        choice = input("What would you like to edit (title/description/due date)? ").strip().lower()
        if choice == 'title':
            new_title = input("Enter new title: ")
            task['title'] = new_title
        elif choice == 'description':
            new_description = input("Enter new description: ")
            task['description'] = new_description
        elif choice == 'due date':
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            task['due_date'] = new_due_date
        else:
            print("Invalid choice.")
    else:
        print("Invalid task index.")

def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted.")
    else:
        print("Invalid task index.")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        index = int(input("Enter task index to edit: "))
        edit_task(index)
    elif choice == '4':
        index = int(input("Enter task index to delete: "))
        delete_task(index)
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
