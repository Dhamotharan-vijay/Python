import pytest
import Sample

def test_sort_list():
    assert Sample.sort_list([0, 1, 2, 0, 1, 2]) == [0,0,1,1,2,2]

def test_sort_list_empty():
    assert Sample.sort_list([]) == []

def test_sort_list_one_element():
    assert Sample.sort_list([0]) == [0]

def test_sort_list_all_zeroes():
    assert Sample.sort_list([0, 0, 0]) == [0, 0, 0]

def test_sort_list_all_ones():
    assert Sample.sort_list([1, 1, 1]) == [1, 1, 1]

def test_sort_list_all_twos():
    assert Sample.sort_list([2, 2, 2]) == [2, 2, 2]

def test_sort_list_only_zeroes_and_ones():
    assert Sample.sort_list([0, 1, 0, 1, 0, 1]) == [0, 0, 0, 1, 1, 1]

def test_sort_list_only_zeroes_and_twos():
    assert Sample.sort_list([0, 2, 0, 2, 0, 2]) == [0, 0, 0, 2, 2, 2]

def test_sort_list_only_ones_and_twos():
    assert Sample.sort_list([1, 2, 1, 2, 1, 2]) == [1, 1, 1, 2, 2, 2]

def test_sort_list_sorted():
    assert Sample.sort_list([0, 0, 1, 1, 2, 2]) == [0, 0, 1, 1, 2, 2]

def test_sort_list_reverse_sorted():
    assert Sample.sort_list([2, 2, 1, 1, 0, 0]) == [0, 0, 1, 1, 2, 2]

def test_sort_list_all_types():
    assert Sample.sort_list([1, 0, 1, 2, 0, 2, 1]) == [0, 0, 1, 1, 1, 2, 2]