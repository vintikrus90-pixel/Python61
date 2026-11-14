# Уровень 3: Продвинутый
#
# Задача: напишите программу, которая позволяет пользователю ввести список оценок,
# затем программа должна выводить среднюю оценку и оценки выше средней.

eva = []
while True:
    toe = input("введите оценку : ") # Enter чтобы завершить
    if toe == "":
        break
    try:
        est = float(toe)
        eva.append(est)
    except ValueError:
        print("ошибка")
if not eva:
    print("Оценки не введины")
else:
    average = sum(eva) / len(eva)
    above_average = [est for est in eva if est > average]

    print(f"Ср оценка : {average:.2f}")
    print("Оценки выше ср : ", above_average)