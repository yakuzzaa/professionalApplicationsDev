from with_standart_functions import chain_search_auto
from manual_realization import chain_replace


def test_simple():
    a, b = [1, 1, 1], [2, 2, 1]
    assert chain_replace(a, b) == chain_search_auto(a, b) == ([2, 2], [1, 1, 1, 1])


def test_empty():
    a, b = [], []
    assert chain_replace(a, b) == chain_search_auto(a, b) == ([], [])


def test_random():
    from utils import random_generate

    a, b = random_generate(5), random_generate(6)
    assert chain_replace(a, b) == chain_search_auto(a, b)


def test_one_list_empty():
    a, b = ([1, 2, 3], [])
    assert chain_replace(a, b) == chain_search_auto(a, b) == ([2, 3], [1])
    b, a = ([1, 2, 3], [])
    assert chain_replace(a, b) == chain_search_auto(a, b) == ([1], [2, 3])
