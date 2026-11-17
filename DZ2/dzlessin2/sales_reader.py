# Домашнее задание 2
# Чтение данных из CSV

import csv

def read_sales(csv_file_path):
    sales = []
    with open(csv_file_path, "r", encoding="utf-8") as csv_file:
        rd = csv.DictReader(csv_file)
        for row in rd:
            sales.append({
                "date": row["Date"],
                "store": row["Store"],
                "product": row["Product"],
                "price": float(row["Price"]),
                "quantity": int(row["Quantity"]),
            })
    return sales