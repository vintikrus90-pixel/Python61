# Домашнее задание 7
# user_manager.py
# Модуль для управления пользователями: добавление, удаление, вывод списка

def add_user(users, name, age):

    if name in users:
        return f"Ошибка: пользователь '{name}' уже существует."
    users[name] = age
    return f"Пользователь '{name}' (возраст {age}) добавлен."


def remove_user(users, name):

    if name not in users:
        return f"Ошибка пользователь '{name}' не найден "
    del users[name]
    return f"Пользователь '{name}' удален "

def list_users(users):

    if not users:
        return "Список пользователей пуст "

    lines = [f"{name} - {age} лет" for name, age in users.items()]
    return "\n".join(lines)
