from operator import index

tasks = []
while True:
    team = input("Введите команду add, remove, list, exit : ")
    if team == "add":
        description = input("Введите описание задачи : ")
        if description:
            tasks.append(description)
            print("Задача добавленина")
        else:
            print("Описание задачи не должно быть пустым")

    elif team == "remove":
        if not tasks:
            print("Список задач пуст")
            continue

        try:
            index = int(input("Введите индекс задачи для удаления : "))
            if 0 <= index < len(tasks):
                remote = tasks.pop(index)
                print(f"задача {remote} удалена")
            else:
                print("Ошибка задачи с таким индексом нет")
        except ValueError:
            print("Ошибка введите индекс числом")

    elif team == "list":
        if tasks:
            print("Список задач : ")
            for index, task in enumerate(tasks):
                print(f"{index}: {task}")
        else:
            print("Список задач пуст")
    elif team == "exit":
        print("Работа программы завершена")
        break
    else:
        print("Неизвестная команда")