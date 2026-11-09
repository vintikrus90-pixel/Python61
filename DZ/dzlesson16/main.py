# Домашнее задание 16
# Консольный интерфейс и обработка команд

from dzlesson16.Employee import Employee
from dzlesson16.Manager import Manager

employees = []

while True:
    cmd = input("Введите команду add>(добавить сотрудника) team>(назначить в команду) show>(показать всех) exit>")

    if cmd == "add":
        name = input("Имя > : ")
        age_raw = input("Возраст > : ")
        position = input("Должность > : ")
        role = input("Сотрудник менеджер (s/m) : ")
        if role == "m":
            employee = Manager(name, int(age_raw), position)
        else:
            employee = Employee(name, int(age_raw), position)
        employees.append(employee)
        print(f'Сотрудник "{name}" добавлен')

    elif cmd == "team":
        manager_name = input("Имя менеджера : ")
        if not any(e.get_name() == manager_name and isinstance(e, Manager) for e in employees):
            continue
        manager = next(e for e in employees if e.get_name() == manager_name and isinstance(e, Manager))

        employee_name = input("Имя сотрудника : ")
        if not any(e.get_name() == employee_name for e in employees):
            continue
        employee = next(e for e in employees if e.get_name() == employee_name)

        manager.add_to_team(employee)
        print(f'Сотрудник "{employee_name}" добавлен в команду "{manager_name}"')

    elif cmd == "show":
        for e in employees:
            print(e.get_info())
            if isinstance(e, Manager):
                e.show_team()

    elif cmd == "exit":
        break
