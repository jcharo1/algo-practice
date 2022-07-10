def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    x = 0
    y = 0

    sorted_input_list = merge_sort(input_list)
    reversed_input_list = sorted_input_list[::-1]
    print(reversed_input_list)

    for i in range(0, len(reversed_input_list),2):
        x = x * 10 + reversed_input_list[i]

    for j in range(1,len(reversed_input_list),2):
        y = y * 10 + reversed_input_list[j]


    return [x,y]


def merge_sort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def merge(left,right):
    merged= []
    left_index = 0 
    right_index = 0 
    

    
    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        
        else:
            merged.append(left[left_index])
            left_index += 1
    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]
    
    
    
    # return the ordered, merged list
    return merged

# Tests
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[],[]])
test_function([[1],[1]])