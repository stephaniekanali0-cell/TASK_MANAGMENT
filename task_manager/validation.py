from datetime import datetime

def validate_task(title, description, due_date):
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty")
    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty")
    if len(due_date.strip()) == 0:
        raise ValueError("Due date cannot be empty")

def validate_task_title(title):
    if title.strip() == "":
        print("Title cannot be empty.")
        return False
    return True
    
def validate_task_description(description):
    if description.strip() == "":
        print("Description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        return False