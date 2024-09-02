import sys
import json
from datetime import datetime

TASK_FILE = "tasks.json"

COMMANDS = ["add"]


def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)    
    except FileNotFoundError:
        print("FileNotFoundError ==>")
        return []
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def main():
    if len(sys.argv) < 2:
        print("usage : main.py <command> [options]")
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("usage: main.py add <description>")
            return
        
        description = sys.argv[2]
        tasks = load_tasks()
        task_id = len(tasks) + 1
        task = {
            "id": task_id,
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }
        tasks.append(task)
        save_tasks(tasks)
        print(tasks)
        print(f"Task Added successfully (ID: {task_id})")

if __name__ == "__main__":
    main()
