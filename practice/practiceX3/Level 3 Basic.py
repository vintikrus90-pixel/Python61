# Уровень 3: Продвинутый
#
# Задача: напишите программу,
# которая позволяет пользователю ввести список оценок,
# затем программа должна выводить среднюю оценку и оценки выше средней.

grades = []

print("Расчет средней оценки и оценок выше среднего")
print("Вводите оценки - (ввод 'done' )")

while True:
    user_input = input("Вводите оценки - (ввод 'done' ) : ")

    if user_input.lower() == "done":
        break

    grade = float(user_input)
    grades.append(grade)

if not grades:
    print("Програма завершает работу")
else:
    average = sum(grades) / len(grades)
    above_average = [grade for grade in grades if grade > average]

    print(f"Список оценок : {grades} ")
    print(f"Средняя оценка : {average:.2f} ")

    if above_average:
        print(f"Оценка выше средней : {above_average} ")
    else:
        print("Оценок выше среднего нет")