from task_manager import add_task, mark_task_as_completed, view_pending_tasks, calculate_progress

def main():
    tasks = []  # shared list that holds all task dictionaries

    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due_date(YYY-MM-DD)")
            try:
                result = add_task(tasks, title, description, due_date)
                print(result)
            except ValueError as e:
                print(e)

        elif choice == "2":
            index = int(input("Enter task index: "))
            try:
                result = mark_task_as_completed(tasks, index - 1)
                print(result)
            except ValueError as e:
                print(e)

        elif choice == "3":
            pending = view_pending_tasks(tasks)
            for task in pending:
                print(task)

        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress:.2f}%")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()