# Домашнее задание 12
# Инициализация структур данных

from collections import deque

tasks = []
help_queue = deque()

while True:
    print("\nРежимы tasks ( задачи ) help (помощь ) exit ( выход )")
    mode = input("Выберите режим : ").strip().lower()

    if mode == "exit":
        print("Выход")
        break

    cmd = input("Команды (add, show, remove/serve) : ").strip().lower()

    if mode == "tasks":
        if cmd == "add":
            t = input("Задача : ").strip()
            if t:
                tasks.append(t)
                print("Добавлено ")
            else:
                print("Пустая задача не добавляется")
        elif cmd == "remove":
            if tasks:
                print("Выполнена : ", tasks.pop())
            else:
                print("Нет задач")
        elif cmd == "show":
            print("Задачи : ", tasks or "пусто")

    elif mode == "help":
        if cmd == "add":
            p = input("Имя : ").strip()
            if p:
                help_queue.append(p)
                print("Добавлен ")
            else:
                print("Имя не может быть пустым")
        elif cmd == "serve":
            if help_queue:
                print("Обслужен : ", help_queue.popleft())
            else:
                print("Очередь пуста ")
        elif cmd == "show":
            print("Очередь : ", list(help_queue) or "пусто")
    else:
        print("Неизвестный режим")