from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word = "half"
    result = count_ocurrences(path, word)
    expected = 107
    assert result == expected

    assert type(result) == int
