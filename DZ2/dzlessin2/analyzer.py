# Домашнее задание 2
# Подсчёт продуктов и выручки по магазинам

def count_products(sales, date):
    product_totals = {}
    for sale in [s for s in sales if s['date'] == date]:
        product_totals[sale['product']] = product_totals.get(sale['product'], 0) + sale['quantity']
    return product_totals

def find_best_store(sales, date):
    store_revenues = {}
    for sale in [s for s in sales if s['date'] == date]:
        store_revenues[sale['store']] = store_revenues.get(sale['store'], 0) + sale['price'] * sale['quantity']
    if store_revenues:
        return None, 0
    best_store = max(store_revenues, key=lambda store: store_revenues[store])
    return best_store, store_revenues[best_store]