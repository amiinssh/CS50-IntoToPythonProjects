import pytest
from seasons import calculate_age_in_minutes, date_to_words


def test_calculate_age_in_minutes():
    assert calculate_age_in_minutes("2000-01-01") == 12614400
    assert calculate_age_in_minutes("2020-01-01") == 2620800


def test_date_to_words():
    assert date_to_words(1) == "one"
    assert date_to_words(21) == "twenty-one"
    assert date_to_words(105) == "one hundred and five"
    assert date_to_words(1005) == "one thousand five"


if __name__ == "__main__":
    pytest.main()
