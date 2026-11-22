# Домашнее задание 3


import unittest


def count_vowels(text: str) -> int:
    """
    test
    :param text:
    text(str): asd
    :return:
    total_count
    """
    total_count = 0
    for vowel in "aeiou":
        total_count += text.lower().count(vowel)
    return total_count


class TestCountVowels(unittest.TestCase):
    def test_regular_string(self):
        self.assertEqual(count_vowels('Hello World'), 3)

    def test_mixed_case(self):
        self.assertEqual(count_vowels('aA eE iI oO uU'), 10)

    def test_empty_string(self):
        self.assertEqual(count_vowels(''), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels('Hll wrld'), 0)

    def test_all_vowels(self):
        self.assertEqual(count_vowels('aeiou'), 5)


if __name__ == "__main__":
    unittest.main()
