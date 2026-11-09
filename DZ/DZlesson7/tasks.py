# Домашнее задание 8
# Менеджер задач на итераторах
tasks = [
    "Сделать домашнюю работу",
    "Помыть посуду",
    "Прочитать книгу"
]

task_iterator = iter(tasks)

print(" Менеджер задач ")
print(" Доступные команды next, list, exit\n" )

while True:
    command = input("Команда : ").strip().lower()

    if command == "next":
        try:
            next_task = next(task_iterator)
            print(f"Выполняем : {next_task}")
        except StopIteration:
            print("Все задачи выполнены")
            break
    elif command == "list":
        remaining_tasks = list(task_iterator)

        if remaining_tasks:
            print("Осталось : ")
            for task in remaining_tasks:
                print(f"{task}")
            task_iterator = iter(remaining_tasks)
        else:
            print("Нет оставшихся задач")
    elif command == "exit":
        print("Прощайте")
        break
    else:
        print("Неизвестная команда Используйте next, list, exit")
