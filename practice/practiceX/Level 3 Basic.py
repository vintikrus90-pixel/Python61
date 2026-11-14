# Получаем строку с числами от пользователя
# Уровень 3: Продвинутый
#
# Задача: напишите программу, которая принимает от пользователя список чисел (вводится одной строкой,
# числа разделены пробелами).
#
# Программа должна:
#
# Использовать итератор для последовательного вывода каждого числа.
# Определить сумму всех чисел, используя цикл с итератором.
# После завершения вывода всех чисел сообщить: «Все числа выведены. Сумма: {сумма}».

input_str = input("Введите числа через пробел : ")

numbers = [int(x) for x in input_str.split()]

iterator = iter(numbers)

total_sum = 0
output_parts = []

while True:
    try:
        num = next(iterator)

        total_sum += num

        output_parts.append(str(num))
    except StopIteration:
        break

number_output = " ".join(output_parts)
print(f"Числа по порядку : {number_output}")
print(f"Все числа выведены сумма : {total_sum}")