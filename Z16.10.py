# 1. Ввод количества транзакций
while True:
    try:
        number_of_transactions = int(input("Введите количество транзакций: "))
        if number_of_transactions > 0:
            break
        elif number_of_transactions == 0:
            print("Количество транзакций не может быть равно нулю. Попробуйте снова.")
        else:
            print("Ошибка: количество транзакций должно быть положительным числом. Попробуйте снова.")
    except ValueError:
        print("Неверный ввод! Пожалуйста, введите целое число.")

# 2. Ввод данных по каждой транзакции
for _ in range(number_of_transactions):
    while True:
        try:
            amount = float(input("Введите сумму транзакции: "))
            if amount >= 0:
                break
            else:
                print("Ошибка: сумма транзакции не может быть отрицательной. Попробуйте снова.")
        except ValueError:
            print("Неверный ввод! Пожалуйста, введите число.")

    description = input("Введите описание операции: ")
    print(f"Транзакция принята: сумма — {amount} руб., описание — '{description}'")

# 3. Финальный вывод
print("\nВсе транзакции успешно учтены!")