# ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# Уровень 2. Средний
# Задача: у вас есть JSON-файл с данными о
# сотрудниках компании, содержащий их имена,
# отделы и зарплаты. Нужно написать программу,
# которая:
# выводит общую сумму зарплат для каждого
# отдела;
# сохраняет результаты в новый JSON-файл.

# подсчёт зарплат по отделам

def calculate_salaries(employees):
    salaries = {}
    for employee in employees:
        department = employee["department"]
        salaries[department] = salaries.get(department, 0) + employee["salary"]
    return salaries
