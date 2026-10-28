# main.py
# Уровень 2: Средний
# Задача: создайте модуль string_utils.py, который содержит функции для работы со строками:
# reverse_string(text) — возвращает перевёрнутую строку. count_vowels(text) — возвращает
# количество гласных букв в строке. is_palindrome(text) — проверяет, является ли строка
# палиндромом (читается одинаково в обоих направлениях). Напишите основную программу,
# которая импортирует этот модуль и предоставляет пользователю выбор функции для работы со строкой.

import string_utils

def main():
    print("=== Утилита для работы со строками ===")
    user_text = input("Введите строку для обработки : ").strip()

    if not user_text:
        print("Ошибка строка не может быть пустой")
        return

    print("\nВыберите действие : ")
    print("1. Перевернуть строку")
    print("2. Посчитать гласные")
    print("3. Проверить на палиндром")

    choice = input("Ваш выбор (1. 2. 3.) : ").strip()

    if choice == "1":
        result = string_utils.reverse_string(user_text)
        print(f"Перевернутая строка: {result}")

    elif choice == "2":
        count = string_utils.count_vowels(user_text)
        print(f"Количество гласных : {count}")

    elif choice == "3":
        if string_utils.is_palindrome(user_text):
            print("Строка является палиндромом")
        else:
            print("Строка не является палиндромом")
    else:
        print("Неверный выбор Допустимы только варианты 1. 2. 3.")

if __name__ == "__main__":
    main()