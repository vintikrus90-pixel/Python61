# Домашнее задание 1 

def extract_numbers(text):
    clean_text = (text.replace(".", " ").replace(",", " ")
                  .replace("–", " ").replace(":", " ")
                  .replace(";", " ").replace("!", " ").replace("?", " "))
    numbers = list(filter(lambda word: word.isdigit(), clean_text.split()))
    result = list(map(lambda i: (i, numbers[i], numbers.count(numbers[i])),
                      range(len(numbers))))
    return result