# Домашнее задание 13
# Точка входа программы интерактивный режим работы с задачами

from DZlesson13.TaskManager import TaskManager

manager = TaskManager()
while True:
    cmd = input("Введите команду < add, done, show exit > : ").strip().lower()
    if cmd == "add":
        title = input("Введите название задачи : ").strip()
        print(manager.add_task(title))

    elif cmd == "done":
        title = input("Введите название задачи : ").strip()
        print(manager.mark_task_done(title))

    elif cmd == "show":
        manager.show_tasks()

    elif cmd == "exit":
        manager.save_to_file()
        break

    print()
