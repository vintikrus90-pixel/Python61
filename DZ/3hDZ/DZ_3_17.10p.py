# Домашнее задание 3
tasks = []

while True:
    team = input("Введите команду add, remove, list, exit : ")

    # Команда add новой задачи
    if team == "add":
        description = input("Введите описание задачи : ")
        if description:
            tasks.append(description)
            print("Задача добавлена")
        else:
            print("Описание не должно быть пустым")

    # Команда remove удаление задачи
    elif team == "remove":
        if not tasks:
            print("Список пуст")
            continue

        try:
            index = int(input("Введите индекс для удаление : "))
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"задача  {removed} удалена ")
            else:
                print("Ошибка с таким индексом нет ")
        except ValueError:
            print("Введите индекс ")

    # Команда list вывод всех задач
    elif team == "list":
        if tasks:
            print("Список задач : ")
            for index, task in enumerate(tasks):
                print(f"{index}: {tasks}")
        else:
            print("Список пуст")
    elif team == "exit":
        print("Программа завершена")
        break