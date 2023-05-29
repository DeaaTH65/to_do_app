# To Do App


class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index!")

    def display_tasks(self):
        print("To-Do List:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}: {task['task']} - {status}")

    def run(self):
        while True:
            print("\n1. Add Task")
            print("2. Complete Task")
            print("3. Display Tasks")
            print("4. Quit")

            choice = input("Enter your choice (1-4): ")
            print()

            if choice == "1":
                task = input("Enter task description: ")
                self.add_task(task)
                print("Task added successfully!")
            elif choice == "2":
                task_index = int(input("Enter task index to mark as completed: "))
                self.complete_task(task_index)
                print("Task marked as completed!")
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")


app = ToDoApp()
app.run()
