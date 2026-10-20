x = 0
while True:
    try:
        num = int(input("Введите число: "))
        if num == 0:
            break

        x += num

    except ValueError:
        print("Ошибка")
print(x)