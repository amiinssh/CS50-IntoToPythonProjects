import pytest
from um import count


def test_count_single_occurrence():
    assert count("Hello, um, world") == 1


def test_count_multiple_occurrences():
    assert count("um um um") == 3


def test_count_case_insensitivity():
    assert count("UM Um uM") == 3


def test_count_no_occurrences():
    assert count("hello world") == 0


def test_count_word_part_of_another():
    assert count("yummy") == 0


def test_count_punctuation():
    assert count("um. Um? um, um!") == 4


if __name__ == "__main__":
    pytest.main()
