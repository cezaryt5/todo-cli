import json
from datetime import datetime
from typing import List, Dict



class todo_app:
    def __init__(self, datafile: str = "/run/media/ceazer/982f53f4-3e3b-4aa6-8864-4f0194b752d01/todo/todo-cli/venv/todo_cli/storage/storage.json"):
        self.data = datafile
        self.tasks: List[Dict] = []
        self.load_data()
    
    def save_data(self):
        with open("todo.json", "w") as f:
            json.dump(self.tasks, f, indent=4)


    def load_data(self):
        try:
            with open("todo.json", "r") as f:
                content = f.read().strip()
                if content:
                    self.tasks = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []


    def add_data(self, description: str):
        with open("todo.json", "w")as f:
            self.tasks.append({
            "id": len(self.tasks) + 1,
            "description": description,
            "completed" : False,
            "created_at": datetime.now().isoformat(),
            "completed_at" : "",
            })
        for i , task in enumerate(1, task):
            task["id"] = i
        print("The task was added succesfully ✅ !!")
        self.save_data()


    def delete_data(self, task_id):
        self.tasks = (task for task in self.tasks if task["id"] != task_id)
        print(f"The task {task_id} was deleted succesfully 🗑️ !!")
        self.save_data()


    def edit(self, task_id: int, New_descr: str):
        for task in self.task : 
            if task["id"] == task_id:
                task["description"] = New_descr
            else :
                print("There is no task with such id")
        self.save_data()


    def completed(self, task_id):
        for task in self.task:
            if task["id"] == task_id:
                task["completed_at"] = datetime.now().isoformat()
            else: 
                print("There is no task with such id")
        print("Thank you for completing the task ✅ !!")
        self.save_data()


    def List(self):
        for task in self.tasks:
            status = "✅" if task["completed"] else "❌"
            print(f"[{status}] {task["id"]} : {task["description"]}")



