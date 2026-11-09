# Домашнее задание 13
# Управление списком задач

import json
import os
from DZlesson13.Task import Task

FILE_NAME = 'tasks.json'

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_from_file()

    def add_task(self,title):
        self.tasks.append(Task(title))
        return f'задача "{title}" добавлена'

    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                return f'Задача "{title}" отмечена как выполненная'
        return f'Задача "{title}" не найдена'

    def show_tasks(self):
        if not self.tasks:
            print("Список пуст")
            return

        for index, task in enumerate(self.tasks, start=1):
            status = "Выполнено" if task.is_done else "Не выполнено"
            print(f'{index}. {task.title} - {status}')

    def save_to_file(self):
        data = [task.to_dict() for task in self.tasks]
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self):
        if not os.path.exists(FILE_NAME):
            return
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            self.tasks.append(Task.from_dict(item))