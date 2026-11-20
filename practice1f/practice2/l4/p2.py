def is_even(number: int) -> bool:
    """
    Проверяет является ли число чётным

    Args:
        number (int): Целое число для проверки

    Returns:
        bool: True если число чётное и False если нечётное
    """
    return number % 2 == 0

print(is_even(4))
print(is_even(7))
print(is_even(-2))
print(is_even(0))
