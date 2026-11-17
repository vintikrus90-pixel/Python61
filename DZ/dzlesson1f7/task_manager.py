# Домашнее задание 17
# Менеджер задач


from decorators import log_action

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.history = []

    @log_action("add task")
    def add_task(self,text):
        self.tasks.append(text)
        self.history.append(("add", text))
        print("Задача добавлена")

    @log_action("show tasks")
    def show_tasks(self):
        if not self.tasks:
            print("Список пуст")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    @log_action("complete tasks")
    def complete_tasks(self, number):
        if not self.tasks:
            print("Список пуст")
            return
        try:
            number = int(number)
        except (ValueError, TypeError):
            print("Ошибка 'должно быть целым числом' ")
            return
        if not 1 <= number <= len(self.tasks):
            print(f"Ошибка с номером {number} нет \nВведите число от 1 до {len(self.tasks)}")
            return
        task = self.tasks.pop(number-1)
        self.history.append(("complete", task, number - 1))
        print("Задача выполнена")

    @log_action("undo")
    def undo(self   ):
        if not self.history:
            print("Нет действий")
            return
        action = self.history.pop()
        if action[0] == "add":
            text = action
            if text in self.tasks:
                self.tasks.remove(text)
            print(f"Отмена : {text}")
        elif action[0] == "complete":
            text, index = action
            self.tasks.insert(index, text)
            print(f"Восстановлен : {text}")

    def run(self):
        print("Введите команду  'add, show, complete, undo, exit' : ")
        while True:
            command = input().strip().lower()
            if command == "add":
                text = input("Введите задачу : ")
                if text:
                    self.add_task(text)
                else:
                    print("Ошибка")
            elif command == "show":
                self.show_tasks()
            elif command == "complete":
                number = input("Введите номер задачи : ")
                self.complete_tasks(number)
            elif command == "undo":
                self.undo()
            elif command == "exit":
                break
