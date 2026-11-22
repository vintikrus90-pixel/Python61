def word_statistics(sentence: str) -> dict[str, int]:
    """
    Возвращает словарь
    :param sentence: строка
    :return: словарь
    """
    result = dict()
    for word in sentence.split():
        if word not in result:
            result[word] = 0
        result[word] += 1
    return result

sentence = "apple banana apple orange banana apple"
print(word_statistics(sentence))