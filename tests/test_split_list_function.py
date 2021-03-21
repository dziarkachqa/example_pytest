from src.src import split_list


def test_sep_none():
    assert split_list(["a","b","c"]) == ("a","b","c"), "Test with list input and sep=None"

def test_separator_not_in_list():
    assert split_list(["a","b","c"],sep='x') == ("a","b","c"), "Test if sep is not in the list"

def test_if_notisinstance():
    assert split_list("string") == "I need list!", "Test with the string input failed"

def test_assign_separator():
    assert split_list(["a","b","c"], sep="a") == ([],["b","c"]), "Test with the assigned separator"

def test_assign_separator1():
    assert split_list(["a","b","c"], sep="b") == (["a"],["c"]), "Test with the assigned separator"