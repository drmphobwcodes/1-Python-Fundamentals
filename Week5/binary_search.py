def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if the_list[mid] == target:
            print("The target is at index", mid)
            return mid
        elif the_list[mid] < target:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(test_list, 10))
print(binary_search(test_list, 4))
print(binary_search(test_list, 33))