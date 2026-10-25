# Домашнее задание 6
# Реестр участников мероприятия
participants = {}

while True:
    cmd = input("\nКоманда add, remove, list, exit : ").strip().lower()

    if cmd == "add":
        data = input("Введите имя и фамилию через пробел : ").strip().split()
        if len(data) < 2:
            print("Ошибка нужно ввести и имя и фамилию")
            continue
        key = (data[0], data[1])
        if key in participants:
            print("Такой участник уже есть")
            continue

        interests_raw = input("Интересы через запятую : ").strip()
        interests = {i.strip() for i in interests_raw.split(",") if i.strip()}
        participants[key] = interests
        print(f"Участник {key[0]} {key[1]} добавлен")

    elif cmd == "remove":
        data = input("Введите имя и фамилию для удаления через пробел : ").strip().split()
        if len(data) < 2:
            print("Ошибка нужно ввести и имя и фамилию.")
            continue
        key = (data[0], data[1])
        if key not in participants:
            print("Участник не найден")
        else:
            del participants[key]
            print(f"Участник {key[0]} {key[1]} удалён")

    elif cmd == "list":
        if not participants:
            print("Реестр пуст")
        else:
            for (fname, lname), interests in participants.items():
                interests_str = ", ".join(sorted(interests)) or "не указаны"
                print(f"{fname} {lname} — интересы: {interests_str}")

    elif cmd == "exit":
        print("Программа завершена")
        break

    else:
        print("Неизвестная команда Используйте add, remove, list, exit")
