from collections import defaultdict

def group_products_by_category(items: list) -> defaultdict:
    if not isinstance(items, list):
        raise TypeError("items must be a list")
    grouped = defaultdict(list)
    for category, product in items:
        grouped[category].append(product)
    return grouped


items1 = [
    ("Фрукты", "Яблоко"),
    ("Овощи", "Морковь"),
    ("Фрукты", "Банан"),
    ("Молочные продукты", "Молоко"),
    ("Овощи", "Картофель")
]

print(group_products_by_category(items1))
