from datetime import datetime

# Import validation functions
from task_manager.validation import(
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = [{"title":"Groceries",
         "description":"Shop at Market Basket for food",
         "due_date":"2024-06-26",
         "completed":True}]

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return
    
    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description":description,
        "due_date":due_date,
        "completed":False

    }

    task.append(task)

    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):

    if 0 <= index < len(tasks):
        tasks[index]["completed"]=True
        print("Task marked as completed")
    else:
      print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    for i, task in enumerate(tasks):
        if not task ["completed"]:
            print(f"\nTask{i}")
            print(f"Tiitle:{task['description']}")
            print(f"Description:{task['description']}")
            print(f"Due Date:{task['due_date']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0
    completed_tasks =0

    for task in tasks:
        if task["completed"]:
            completed_tasks += 1
    progress = (completed_tasks/len(tasks))*100
    return progress