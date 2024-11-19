import pytest

from main import get_top_mentors


@pytest.mark.parametrize("result", [
    ("Евгений: 2 раз(а), Максим: 1 раз(а), Александр: 1 раз(а)"),
    ("Евгений: 2 раз(а), Денис: 1 раз(а), Александр: 1 раз(а)"),
    ("Владимир: 2 раз(а), Евгений: 2 раз(а), Роман: 2 раз(а)"),
    ("Александр: 1 раз(а), Владимир: 1 раз(а), Роман: 1 раз(а)"),
])
def test_get_top_mentors(result):
    assert get_top_mentors() == result
