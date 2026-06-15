from datetime import datetime

# Import validation functions
from task_manager.validation import validate_task

# Define tasks list
tasks = [{"title":"Groceries",
         "description":"Shop at Market Basket for food",
         "due_date":"2024-06-26",
         "completed":True}]

# Implement add_task function
def add_task(tasks, title, description, due_date):
    validate_task(title, description, due_date)
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    return "Task added successfully!"



    
# Implement mark_task_as_complete function
def mark_task_as_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return "Task marked as complete!"
    raise ValueError("Invalid task index")


    
# Implement view_pending_tasks function
def view_pending_tasks(tasks):
    return [t for t in tasks if not t["completed"]]



# Implement calculate_progress function
def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0.0
    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100

