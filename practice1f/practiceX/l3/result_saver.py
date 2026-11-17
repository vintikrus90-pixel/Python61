# ПРАКТИЧЕ СКАЯРАБОТА№ РАБОТА С ФОРМАТАМИ CSV, jSON
# Уровень 3. Продвинутый
# Задача: дано два файла. В
# первом products.csv содержатся данные о
# количестве продуктов, во втором
# файле prices.json — стоимости этих продуктов.
# Нужно создать новый JSON-файл, в котором будут
# указаны продукты, их количество и общая
# стоимость.

# сохранение итогового JSON

import json

def save_result(result, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(obj=result,
                  fp=file,
                  indent=4,
                  ensure_ascii=False)
