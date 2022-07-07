items = [8, 3, 1, 7, 0, 10, 2]
# select the last element as the pivot


def sort_a_lil_bit(items):
    pivot_index = len(items)-1
    pivot_element= items[pivot_index]


    left_index = 0

    while (pivot_index != left_index):
        
        item = items[left_index]
        

        if item <= pivot_element:
            left_index += 1
            continue

        items[left_index] = items[pivot_index-1]
        

        items[pivot_index-1] = pivot_element
        items[pivot_index] = item
        pivot_index -= 1

    return print(pivot_index)

sort_a_lil_bit(items)
print(sort_a_lil_bit)
