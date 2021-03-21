from src.src import join_list


def test_basic_string():
    assert join_list(["a","b","c"]) == "abc", "Test with list of strings failed"

def test_if_notisinstance():
    assert join_list("string") == "I need list!", "Test with the string input failed"

def test_type():
    assert type(join_list(["a","b","c"])) == str, "Test to check the output type"

def test_empty_list():
    assert join_list([]) == "", "Test if input is empty list"
