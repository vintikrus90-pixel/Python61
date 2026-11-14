from functools import reduce

def calculate_total(cart):
    item_totals = map(lambda i: i[0] * i[1], cart)
    total = reduce(lambda a,b: a+b, item_totals, 0)
    return total

cart = [(10.99, 2), (5,49, 4), (3.99, 1)]
print(calculate_total(cart))
print(calculate_total([(15, 1), (5, 4), (1, 10)]))

def combine_employee_data(names, positions, salaries):
    l = zip(names, positions, salaries)
    res = map(lambda i: f"{i[0]}-{i[1]}-{i[2]}", l)
    return list(res)

    # return [f"имя-должность-зарплата", f"имя-должность-зарплата", f"имя-должность-зарплата"]
nms = ["Вася", "Оля", "Андрей"]
pstns = ["Маляр", "Плотник", "Механик"]
slrs = ["100", "100", "200тыс."]

print(combine_employee_data(nms, pstns, slrs))
