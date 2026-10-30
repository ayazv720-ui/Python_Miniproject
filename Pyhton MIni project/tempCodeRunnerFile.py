import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
            print("Task added successfully!")

        elif choice == "2":
            if not tasks:
                print("No tasks found.")
            for i, item in enumerate(tasks, 1):
                status = "Completed" if item["done"] else "Pending"
                print(f"{i}. {item['task']} - {status}")

        elif choice == "3":
            try:
                n = int(input("Enter task number: "))
                if 1 <= n <= len(tasks):
                    tasks[n - 1]["done"] = True
                    save_tasks(tasks)
                    print("Task completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")

        elif choice == "4":
            try:
                n = int(input("Enter task number: "))
                if 1 <= n <= len(tasks):
                    tasks.pop(n - 1)
                    save_tasks(tasks)
                    print("Task deleted!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")

        elif choice == "5":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()