# # ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# # Уровень 1. Базовый
# # Задача: прочитать CSV-файл с данными о
# # студентах и вывести средний балл по каждому
# # предмету.

from practice1f.practiceX.l1.data_reader import read_students
from stats_calculator import calculate_averages

headers, rows = read_students("students.csv")
averages = calculate_averages(headers, rows)

for subject, avg in averages.items():
    print(f"{subject}: {avg:.1f}")