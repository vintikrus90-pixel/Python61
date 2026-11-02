# Домашнее задание 9
# Функция-генератор: возвращает числа в диапазоне [start, end, even=True]

def number_sequence(start, end, even=True ):
    for number in range(start, end + 1):
        if (number % 2 == 0) == even:
            yield number

while True:
    try:
        start = int(input("Введите начало диапазона : "))
        end = int(input("Введите конец диапазона : "))
        break
    except ValueError:
        print("Ошибка Введите целое число\n")

choice = input("Введите ( чет ) или ( нечет ) : ").strip().lower()

if choice == "чет" :
    even_flag = True
elif choice == "нечет" :
    even_flag = False

label = "четные" if even_flag else "нечетные"
print(f"\n {label} числа от {start} до {end} : ")

for number in number_sequence(start, end, even_flag):
    print(number)

def number_sequence2(start, end, even=True):
    return [number for number in range(start, end + 1) if (number % 2 == 0) == even]

print(f"{label} чисда от {start} до {end} (через генераторное выражение) : ")
print(number_sequence2(start, end, even_flag))