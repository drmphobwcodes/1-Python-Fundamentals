"""
Binary Search Example
"""


def binary_search(the_list, target):
    """
    Performs a binary search

    Arguments
    the_list : a list to search
    target : the target to search for

    Returns location or None
    """

    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return the_list[pivot]
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1

    return None


my_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
print(binary_search(my_list, 10))
print(binary_search(my_list, 5))
print(binary_search(my_list, 33))
