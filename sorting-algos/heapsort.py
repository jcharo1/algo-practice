
items = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]

def heapsort(arr):
        # First convert the array into a maxheap by calling heapify on each node, starting from the end   
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
    
def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
    
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node
    
    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    if largest_index != i :
        # arr[i] = arr[largest_index]
        # arr[largest_index]= arr[i]
        arr[i], arr[largest_index] = arr[largest_index], arr[i] 

        heapify(arr, n , largest_index)
    print(items)
print(heapsort(items))
