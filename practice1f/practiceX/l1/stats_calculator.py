# ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# Уровень 1. Базовый
# Задача: прочитать CSV-файл с данными о
# студентах и вывести средний балл по каждому
# предмету.

def calculate_averages(headers, rows):
    averages = {}
    for i in range(1, len(headers)):
        subject = headers[i]
        scores = [int(row[i]) for row in rows]
        averages[subject] = sum(scores) / len(scores)
    return averages