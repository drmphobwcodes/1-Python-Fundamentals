'''Bubble Sort Example'''
unsorted_list = [101, 49, 3, 12, 56]


def bubblesort(the_list):
    '''Bubble sort'''
    high_idx = len(the_list) - 1

    for i in range(high_idx):
        list_changed = False
        for j in range(high_idx):
            _item = the_list[j]
            _next = the_list[j+1]

            if _item > _next:
                the_list[j] = _next
                the_list[j+1] = _item
                list_changed = True

            print(the_list, i, j)
        print(list_changed)
        if list_changed is False:
            break


bubblesort(unsorted_list)
