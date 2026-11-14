import csv

total = lambda q, p: q * p

total_revenue = 0
with open("data.csv", "r", encoding="utf-8") as csv_file:
    rd = csv.DictReader(csv_file)
    for row in rd:
        total_revenue += total(int(row["quantity"]), float(row["price"]))

print(f"Общий доход: {total_revenue}")
