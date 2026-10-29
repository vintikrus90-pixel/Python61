# Уровень 3: Продвинутый
# Задача: разработайте программу для подсчета среднего количества товаров,
# поступивших на склад за указанное количество дней.
# Программа должна сначала запрашивать у пользователя количество дней для анализа.
# Затем для каждого дня должна запрашиваться количество товаров, поступивших на склад.
# В конце программа должна вывести среднее количество товаров, поступивших за день.
# Если ввод данных некорректен (например, введено отрицательное число дней или товаров,
# или нечисловое значение), программа должна сообщать об ошибке и предлагать повторный ввод.

def get_positive_numbers(prompt):
    ["Запрашивает у пользователя положительное число повторяет запрос при ошибке"]
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value <= 0:
                print("Ошибка")
                continue
            return value
        except ValueError:
            print("Ошибка")

def get_non_negative_numbers(prompt):
    ["Запрашивает неотрицательное число (0 и выше)"]
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value < 0:
                print("Ошибка")
                continue
            return value
        except ValueError:
            print("ошибка")

print("Программа подсчета среднего количества товаров за дней")

days = int(get_positive_numbers("Введите количество дней : "))

total_items = 0

for day in range(1, days + 1):
    while True:
        quantity = get_non_negative_numbers(f"Введите количество товаров поступивших в день {day} : ")
        total_items += quantity
        break

average = total_items / days

print(f"\nОбщее количество товаров за {day} дней : {total_items}")
print(f"Среднее количество товаров в день : {average:.2f}")