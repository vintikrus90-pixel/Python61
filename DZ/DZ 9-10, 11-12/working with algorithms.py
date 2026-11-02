# Домашнее задание 11
# Программа демонстрирует работу с алгоритмами и структурами данных

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def count_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count

while True:
    raw = input("Введите список чисел через пробел : ").strip()
    parts = raw.split()
    try:
        numbers = [int(p) for p in parts]
        break
    except ValueError:
        print("( Ошибка ) неверный ввод (не целое число)")

print("Ваш список : ", numbers)

if len(numbers) == 0:
    print("Список пуст")
else:
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    print("Максимальное значение в списке : ", maximum)

sorted_numbers = selection_sort(numbers.copy())
print("Отсортированный список : ", sorted_numbers)

target_raw = input("Введите число для поиска : ").strip()
target = int(target_raw)

occurrences = count_occurrences(sorted_numbers, target)
print(f"Число {target} встречается {occurrences} раз(а) в списке")