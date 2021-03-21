from src.src import common_elements


# def common_elements(lst1: list, lst2: list) -> list:
#     """Function for finding common elements"""
#     temp = set(lst2)
#     lst3 = [value for value in lst1 if value in temp]
#     return lst3

def test_common_elements():
    assert common_elements(['apple','banana','beet'],['sheep','fish','beet','bird']) == ['beet'],"Find common element test"

def test_type():
    assert type(common_elements(['a','b','c'],['a','f','g'])) == list, 'Test type of output'

def test_no_common():
    assert  common_elements(['a','b','c'], ['d','f','e']) == []   ,"Test if no common elements"

def test_repeated_elements():
    assert common_elements(['a','a','a'],['a']) == ['a','a','a'], "Test repeated elements"

def test_repeated_elements1():
    assert common_elements(['a'],['a','a','a']) == ['a'], "Test repeated elements"