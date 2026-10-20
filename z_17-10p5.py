float_sum = 0
while True:
    try:
        num = int(input("Введите число: "))
        if num == 0:
            break

        float_sum += num

    except ValueError:
        print("gdfg")
print(float_sum)