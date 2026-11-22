# Домашнее задание 6

def is_balanced(string):
    if string == "":
        return True
    if string[0] not in "([{":
        return False
    for pair in ("()", "[]", "{}"):
        if pair in string:
            return is_balanced(string.replace(pair, "", 1))
    return False

print(is_balanced("([])"))
print(is_balanced("([)]"))