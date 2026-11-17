# Домашнее задание 2
# Основная программа

from sales_reader import read_sales
from analyzer import count_products, find_best_store
from report import generate_report, save_report

try:
    sales = read_sales("sales_data.csv")
except FileNotFoundError:
    print("Ошибка")
    exit()
except (KeyError, ValueError):
    print("Ошибка")
    exit()

date = input("Введите дату 'YYYY - MM - DD' : ")

day_sales = [s for s in sales if s["date"] == date]
if not day_sales:
    print(f"Ошибка {date} продаж нет ")
    exit()

product_totals = count_products(sales, date)
best_store, revenue = find_best_store(sales, date)
print(f"Продажи за {date} : {best_store} обьем {revenue:.0f}")

report = {date: generate_report(product_totals)}
save_report(report, "sales_report.json")
print("Отчет сохранен в файле sales_report.json")
