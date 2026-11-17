# ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# Уровень 3. Продвинутый
# Задача: дано два файла. В
# первом products.csv содержатся данные о
# количестве продуктов, во втором
# файле prices.json — стоимости этих продуктов.
# Нужно создать новый JSON-файл, в котором будут
# указаны продукты, их количество и общая
# стоимость.

# точка входа

from data_loader import read_products, read_prices
from cost_calculator import calculate_totals
from result_saver import save_result

products = read_products("products.csv")
prices = read_prices("prices.json")

result = calculate_totals(products, prices)
save_result(result, "products_with_total.json")

print("Отчёт сохранён в файле products_with_total.json")
