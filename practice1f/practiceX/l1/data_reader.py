# ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# Уровень 1. Базовый
# Задача: прочитать CSV-файл с данными о
# студентах и вывести средний балл по каждому
# предмету.

import csv

def read_students(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
    return header, rows