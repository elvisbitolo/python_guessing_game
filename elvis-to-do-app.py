# Elvis's To-Do App
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['title']}")

def add_task():
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Task '{title}' added.")

def mark_done():
    show_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num-1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

while True:
    print("\nTo-Do App Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
