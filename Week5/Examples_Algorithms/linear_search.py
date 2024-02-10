"""
Linear Search Examples
"""


def linear_search(the_list, target):
    """
    Performs a linear search

    Arguments
    the_list : a list to search
    target : the target to search for

    Returns location or None
    """

    for idx, val in enumerate(the_list):
        if val == target:
            _t = f"Found {val} at index {idx}"
            print(_t)
            return idx
    print("Target is not in the list")
    return None


my_list = [6, 3, 4, 2, 5, 7]
linear_search(my_list, 5)
linear_search(my_list, 3)
linear_search(my_list, 8)


def linear_search_dict(the_dict, target):
    """
    Performs a linear search on a dictionary

    Arguments
    the_dict : a dictioiinary to search
    target : the target to search for

    Returns key or None
    """

    for key in the_dict:
        if the_dict[key] == target:
            print(f"Found {the_dict[key]} at key {key}")
            return key
    print("Target is not in the dict")
    return None


my_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}
linear_search_dict(my_dict, 5)
linear_search_dict(my_dict, 3)
linear_search_dict(my_dict, 8)
