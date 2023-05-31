from tasks import tasks

# Access and use the tasks list
for task in tasks:
    print(f"Name: {task['name']}")
    print(f"Priority: {task['priority']}")
    print(f"Type: {task['type']}")
    print(f"Command: {task['command']}")
    print("---")
