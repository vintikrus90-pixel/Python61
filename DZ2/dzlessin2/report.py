# Домашнее задание 2
# Формирование отчёта и сохранение в JSON

import json

def generate_report(product_totals):
    return [{"product" : product, "total_sales" : total_sales} for product, total_sales in product_totals.items()]

def save_report(report, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(obj=report, fp=file, indent=4, ensure_ascii=False)