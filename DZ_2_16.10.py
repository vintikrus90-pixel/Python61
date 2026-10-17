# 1 Ввод количества учебных дней
while True:
    try:
        num_days_input = input("Введите количество учебных дней от 1 до 7 : ")
        num_days = int(num_days_input)
        if 1 <= num_days <= 7:
            break
        else:
            print("Ошибка: количество дней должно быть от 1 до 7 Введите снова")
    except ValueError:
        print("Ошибка: введите число Введите снова")
total_hours = 0

# 2 Ввод часов для каждого дня
for day in range(1, num_days + 1):
    while True:
        try:
            hours_input = input(f"Сколько часов учились в день {day} : ")
            hours = float(hours_input)
            if hours > 0:
                total_hours += hours
                break
            else:
                print("ошибка: количество часов должно быть числом Введите снова")
        except ValueError:
            print("Ошибка: введите число Введите снова")
# 3 Вывод результата
print(f"Учет завершен Дней - {num_days}, общее время - {total_hours}")
print("\nВсе записи успешно добавлены")