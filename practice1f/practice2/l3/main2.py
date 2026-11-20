def count_punct_marks(string: str) -> int:
    """
    test
    :param string:
    strign(str): asd
    :return:
    total_conut
    """
    total_count = 0
    for sym in ",.:;":
        total_count += string.count(sym)
    return total_count

def test_empty_string():
    assert count_punct_marks('') == 0

def test_no_punctuation():
    assert count_punct_marks('Hello world') == 0

def test_single_punctuation():
    assert count_punct_marks('Hello world!') == 1

def test_multiple_punctuation():
    assert count_punct_marks('Hello, world! How are you?') == 3

def test_edge_case():
    assert count_punct_marks('!!!') == 3

def test_all_punctuation():
    assert count_punct_marks(".,:;!?") == 6