import pytest


def calculate_square(a):
    perimeter = a * 4
    area = a ** 2
    return ('Периметр:', perimeter), ('Площадь:', area)


@pytest.mark.parametrize("a, expected_result", [(2, ('Периметр:', 8), ('Площадь:', 4)),
                                                (4, ('Периметр:', 16), ('Площадь:', 16)),
                                                (6, ('Периметр:', 24), ('Площадь:', 36))])
def test_calculate_square(a, expected_result):
    assert calculate_square(a) == expected_result
