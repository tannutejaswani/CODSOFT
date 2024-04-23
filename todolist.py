class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. [{'X' if task['completed'] else ' '}] {task['task']}")
    def mark_task_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]['completed'] = True
        else:
            print("Invalid task index.")
    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
        else:
            print("Invalid task index.")
def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            print("Your To-Do List:")
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_task_completed(index)
            print("Task marked as completed.")
        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)
            print("Task deleted successfully.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
