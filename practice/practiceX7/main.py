from collections import Counter
c1 = Counter(a=2, b=1, c=3)
c2 = Counter(a=1, b=2, d=3)
print(c1 & c2)
print(c1 | c2)

counter = Counter({"a": 2, "b": 3})
print(counter)  # Вывод: Counter({'a': 2, 'b': 3})