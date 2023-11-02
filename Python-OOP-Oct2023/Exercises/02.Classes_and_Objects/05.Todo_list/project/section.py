from typing import List
from project.task import Task



class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        # tasks_list = list(filter(lambda t: t.name, self.tasks))  # !!!!!
        tasks_found = [t for t in self.tasks if t.name == task_name]
        if not tasks_found:
            return f"Could not find task with the name {task_name}"
        task = tasks_found[0]
        task.completed = True
        return f'Completed task {task.name}'

    def clean_section(self):
        # completed_list = list(filter(lambda t: t.completed, self.tasks))  # !!!!!
        completed_list = [t for t in self.tasks if t.completed]
        for task in completed_list:
            self.tasks.remove(task)
        return f"Cleared {len(completed_list)} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += task.details() + '\n'
        return result
