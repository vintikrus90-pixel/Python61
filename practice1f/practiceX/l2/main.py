# ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# Уровень 2. Средний
# Задача: у вас есть JSON-файл с данными о
# сотрудниках компании, содержащий их имена,
# отделы и зарплаты. Нужно написать программу,
# которая:
# выводит общую сумму зарплат для каждого
# отдела;
# сохраняет результаты в новый JSON-файл.

# точка входа, вывод результата

from employee_reader import read_employees
from salary_calculator import calculate_salaries
from report_saver import save_report

employees = read_employees("employees.json")
salaries = calculate_salaries(employees)

for department, total in salaries.items():
    print(f"{department}: {total}")

save_report(salaries, "department_salaries.json")
