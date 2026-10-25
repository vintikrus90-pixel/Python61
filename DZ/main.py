# Домашнее задание 7
# main.py
# Основная программа: командный интерфейс для управления пользователями
from user_manager import add_user, remove_user, list_users

def get_age():

    age_input = input("Введите возраст (целое число) : ").strip()
    try:
        age = int(age_input)
        if age < 0:
            print("Ошибка возраст не может быть отрицательным")
            return None
        return age
    except ValueError:
        print("Ошибка возраст должен быть целым числом")
        return None

def main():
    users = {}

    print("Управление пользователями (Доступные команды add, remove, list, exit)")
    while True:
        command = input("\nВведите команду : ").strip().lower()
        if command == "add":
            name = input("Введите имя пользователя : ").strip()
            if not name:
                print("Ошибка имя не может быть пустым")
                continue

            age = get_age()
            if age is None:
                continue
            result = add_user(users, name, age)
            print(result)

        elif command == "remove":
            name = input("Введите имя пользователя для удаления : ").strip()
            if not name:
                print("Ошибка имя не может быть пустым")
                continue
            result = remove_user(users, name)
            print(result)

        elif command == "list":
            result = list_users(users)
            print("\nСписок пользователей : ")
            print(result)

        elif command == "exit":
            print("Программа завершена")
            break

        else:
            print("Неизвестная команда Используйте add, remove, list, exit")

if __name__ == "__main__":
    main()
