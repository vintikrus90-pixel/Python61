# ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# Уровень 2. Средний
# Задача: у вас есть JSON-файл с данными о
# сотрудниках компании, содержащий их имена,
# отделы и зарплаты. Нужно написать программу,
# которая:
# выводит общую сумму зарплат для каждого
# отдела;
# сохраняет результаты в новый JSON-файл.

# сохранение отчёта в JSON

import json

def save_report(report, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(obj=report,
                  fp=file,
                  indent=4,
                  ensure_ascii=False)
