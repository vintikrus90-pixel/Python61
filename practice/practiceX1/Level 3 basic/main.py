# main.py
# Уровень 3: Продвинутый
# Задача: создайте модуль temperature_converter.py, который содержит функции:
# celsius_to_fahrenheit(c) — переводит температуру из Цельсия в Фаренгейт.
# fahrenheit_to_celsius(f) — переводит температуру из Фаренгейта в Цельсий.
# kelvin_to_celsius(k) — переводит температуру из Кельвина в Цельсий. Напишите программу,
# которая позволяет пользователю выбрать тип конверсии и вводит температуру для преобразования.

import temperature_converter

def get_float_input(prompt:str) -> float:
    ["Запрашивает у пользователя число и проверяет коректность ввода"]
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка введите коретное число")

def main():
    print("Конвертер температур")
    print("Доступные варианты конверсии : ")
    print("1. Цельсий → Фаренгейт")
    print("2. Фаренгейт → Цельсий")
    print("3. Кельвин → Цельсий")

    choice = input("Выберите варианты (1. 2. 3.) : ").strip()

    if choice == "1":
        c = get_float_input("Введите температуру в градусах цельсия : ")
        if c < -273.15:
            print("Ошибка тем.ниже нуля невозможна")
            return
        result = temperature_converter.celsius_to_fahrenheit(c)
        print(f"{c:.2f} °C = {result:.2f} °F")

    elif choice == "2":
        f = get_float_input("введите темп. в градусах фаренгейта : ")
        if f < -459.67:
            print("Ошибки темп. ниже абсолютного нуля невозможна")
            return
        result = temperature_converter.fahrenheit_to_celsius(f)
        print(f"{f:.2f} °F = {result:.2f} °C")

    elif choice == "3":
        k = get_float_input("Введите темп. в кельвинах : ")
        if k < 0:
            print("Ошибка темп. ниже абсолютного нуля невозможна")
            return
        result = temperature_converter.kelvin_to_celsius(k)
        print(f"{k:.2f} K = {result:.2f} °C")

    else:
        print("Неверный выбор допустимы только варианты 1. 2. 3. ")

if __name__ == "__main__":
    main()