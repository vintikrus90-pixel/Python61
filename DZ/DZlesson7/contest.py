# Домашнее задание 5
# Анализ участников

event1_guests = input(" Учачтники 1-го конкурса (через пробел) : ").strip().split()
event2_guests = input(" Участники 2-го конкурса (через пробел) : ").strip().split()
event3_guests = input(" Участники 3-го конкурса (через пробел) : ").strip().split()

s1 = set(event1_guests)
s2 = set(event2_guests)
s3 = set(event3_guests)

all_three = s1 & s2 & s3

any_one = s1 | s2 | s3

only_one = (s1 - s2 - s3) | (s2 - s1 - s3) | (s3 - s1 - s2)

exactly_two = (s1 & s2 - s3) | (s1 & s3 - s2) | (s2 & s3 - s1)

print("\n Результаты ")
print(f" Участники всех трёх конкурсов : {all_three}")
print(f" Участники хотя бы одного конкурса : {any_one}")
print(f" Участники только одного конкурса : {only_one}")
print(f" Участники ровно двух конкурсов : {exactly_two}")