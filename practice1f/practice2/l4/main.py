def count_unique(int_list: list[int]) -> dict[int, int]:
    """
    Возвращает словарь, где ключом является некоторое число, а значением счетчик дублирущих в списке

    :param int_list: список чисел
    :return: словарь
    """
    result = dict()
    for item in int_list:
        if item not in result:
            result[item] = 0
        result[item] += 1
    return result