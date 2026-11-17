# ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# Уровень 3. Продвинутый
# Задача: дано два файла. В
# первом products.csv содержатся данные о
# количестве продуктов, во втором
# файле prices.json — стоимости этих продуктов.
# Нужно создать новый JSON-файл, в котором будут
# указаны продукты, их количество и общая
# стоимость.

# расчёт общей стоимости

def calculate_totals(products, prices):
    result = {}
    for item in products:
        product = item["product"]
        quantity = item["quantity"]
        price = prices[product]
        result[product] = {
            "quantity": quantity,
            "total_cost": quantity * price,
        }
    return result

