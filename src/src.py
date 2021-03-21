def join_list(some_list: list) -> str:
    """Function joins list elements and strings"""
    if not isinstance(some_list, list):
        return "I need list!"
    return "".join([str(el) for el in some_list])

def split_list(some_list: list, sep=None) -> tuple:
    """Function for splitting list by separator"""
    if not isinstance(some_list, list):
        return "I need list!"
    if sep is None or sep not in some_list:
        return tuple(some_list)
    return (some_list[:some_list.index(sep)], some_list[some_list.index(sep)+1:])

def common_elements(lst1: list, lst2: list) -> list:
    """Function for finding common elements"""
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3
