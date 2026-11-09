# Домашнее задание 14
# Демонстрация работы с векторами

from DZlesson14.Vector2D import Vector2D

v1 = Vector2D(3, 4)
v2 = Vector2D(1, -2)

print(f"Сложение: {v1 + v2}")
print(f"Вычитание: {v1 - v2}")
print(f"Длина вектора: {v1.length()}")
print(f"Строковое представление: {v1}")