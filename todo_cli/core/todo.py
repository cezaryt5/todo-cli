"""Core todo application logic."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional


class TodoApp:
    """A simple todo application with JSON storage."""
    
    def __init__(self, data_file: Optional[str] = None):
        """
        Initialize the TodoApp with a data file path.
        
        Args:
            data_file: Path to the JSON file for storing tasks.
                      Defaults to ~/.todo_cli/tasks.json
        """
        if data_file is None:
            home_dir = Path.home()
            data_dir = home_dir / ".todo_cli"
            data_dir.mkdir(exist_ok=True)
            self.data_file = str(data_dir / "tasks.json")
        else:
            self.data_file = data_file
            
        self.tasks: List[Dict] = []
        self.load_data()
    
    def load_data(self) -> None:
        """Load tasks from the JSON file."""
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    self.tasks = json.loads(content)
                else:
                    self.tasks = []
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
    
    def save_data(self) -> None:
        """Save tasks to the JSON file."""
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)
    
    def add_task(self, description: str) -> int:
        """
        Add a new task.
        
        Args:
            description: The task description.
            
        Returns:
            The ID of the newly created task.
        """
        task_id = 1 if not self.tasks else max(t["id"] for t in self.tasks) + 1
        
        task = {
            "id": task_id,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        
        self.tasks.append(task)
        self.save_data()
        return task_id
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.
        
        Args:
            task_id: The ID of the task to delete.
            
        Returns:
            True if deleted, False if not found.
        """
        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        
        if len(self.tasks) < original_count:
            self.save_data()
            return True
        return False
    
    def edit_task(self, task_id: int, new_description: str) -> bool:
        """
        Edit a task's description.
        
        Args:
            task_id: The ID of the task to edit.
            new_description: The new description.
            
        Returns:
            True if edited, False if not found.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                self.save_data()
                return True
        return False
    
    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id: The ID of the task to complete.
            
        Returns:
            True if completed, False if not found.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat()
                self.save_data()
                return True
        return False
    
    def get_tasks(self, include_completed: bool = True) -> List[Dict]:
        """
        Get all tasks.
        
        Args:
            include_completed: Whether to include completed tasks.
            
        Returns:
            List of tasks.
        """
        if include_completed:
            return self.tasks
        return [task for task in self.tasks if not task["completed"]]
    
    def get_task(self, task_id: int) -> Optional[Dict]:
        """
        Get a specific task by ID.
        
        Args:
            task_id: The task ID.
            
        Returns:
            The task dict or None if not found.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None