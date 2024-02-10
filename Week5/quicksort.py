my_list=[6,3,4,2,5,7]

def sort_part(the_list, low_idx, pivot_idx):
    pivot_value = the_list[pivot_idx]
    
    while pivot_idx != low_idx:
        low_val = the_list[low_idx]

        print(the_list, low_val, pivot_value)
        if low_val <= pivot_value:
            low_idx += 1
        else:
            the_list[low_idx] = the_list[pivot_idx - 1]
            the_list[pivot_idx] = low_val
            the_list[pivot_idx - 1] = pivot_value
            pivot_idx -= 1
    return pivot_idx

def quicksort(the_list, low_idx, high_idx):
    if low_idx < high_idx:
        return
    pivot = sort_part(the_list, low_idx, high_idx)
    quicksort(the_list, low_idx, pivot - 1)
    quicksort(the_list, pivot + 1, high_idx)

quicksort(my_list, 0, len(my_list) - 1)
print("my_list:", my_list)

