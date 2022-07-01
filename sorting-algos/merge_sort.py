# MergeSort
# MergeSort is a divide and conquer algorithm that divides a list into equal halves until it has two single elements and then merges the sub-lists until the entire list has been reassembled in order.

# Divide
# Our MergeSort code will focus first on the divide portion of the algorithm. If the list we receive has only a single element in it, the list can be considered sorted and we can return immediately. This is our recursion base case. If we have more than 1 element we need to split the list into equal halves and call MergeSort again for each half.

# Conquer
# Once you have split the list down to single elements, your mergesort will start merging lists, in order, until you have reassembled the entire list in order.

# Design
# First, let's sketch this out. It's clear we want a recursive function, but how will it govern its recursion?

def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))
# We have decomposed the problem, now we will address each piece separately.

# Divide
# We can use python's // operator to find a midpoint. If items's length is even, we will have the midpoint. If items's length is odd, we will have one half larger by one.