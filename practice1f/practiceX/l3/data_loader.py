# ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# Уровень 3. Продвинутый
# Задача: дано два файла. В
# первом products.csv содержатся данные о
# количестве продуктов, во втором
# файле prices.json — стоимости этих продуктов.
# Нужно создать новый JSON-файл, в котором будут
# указаны продукты, их количество и общая
# стоимость.

# чтение CSV и JSON

import csv
import json

def read_products(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as file:
        rd = csv.DictReader(file)
        for row in rd:
            products.append({
                "product": row["Product"],
                "quantity": int(row["Quantity"]),
            })
    return products

def read_prices(filename):
    with open(filename, "r", encoding="utf-8") as file:
        prices = json.load(fp=file)
    return prices
