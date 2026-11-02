# Домашнее задание 10
# Программа для работы с текстовым файлом для хранения заметок.

import os

filename = "notes.txt"

while True:
    print("\nКоманды create, add, view, exit")
    cmd = input("Введите команду : ").strip().lower()

    if cmd == "create":
        with open(filename, "w", encoding="utf-8") as file:
            pass
        print(f"Файл '{filename}' создан и очищен")

    elif cmd == "add":
        note = input("Введите текст заметки : ").strip()
        if not note:
            print("Заметки не может быть пустой")
        else:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(note + "\n")
            print("Заметка добавлена")

    elif cmd == "view":
        if not os.path.exists(filename):
            print("Файл не найден Сначала создайте файл")
        else:
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    lines = file.readlines()

                if not lines:
                    print("Файл пуст")
                else:
                    print("\n Список заметок ")
                    for idx, line in enumerate(lines, start=1):
                        print(f"{idx}. {line.strip()}")
                    print("-------------------------")
            except FileNotFoundError:
                print("Файл не найден")
            except IOError:
                print("Ошибка ввода вывода")

    elif cmd == "exit":
        print("Программа завершена")
        break

    else:
        print("Неизвестная команда")