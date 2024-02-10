def linear_search_dictionary(the_dict, target):
    for key in the_dict:
        if the_dict[key] == target:
            print("The target is at key", key)
            return key
    print("The target is not in the dictionary")
    return -1

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)