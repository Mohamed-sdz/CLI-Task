# task.py

class Task:
    def __init__(self, title, description, priority, due_date, status):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f'Task: {self.title}\nPriority: {self.priority}\nDue Date: {self.due_date}\nStatus: {self.status}'

# Add more methods for task management as needed
