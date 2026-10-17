total_sum = 0
while True:
    try:
        num = int(input("Введите число: "))
        if num == 0:
            break

        total_sum += num

    except ValueError:
        print("gdfg")
print(total_sum)