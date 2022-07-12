

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1
    if type(input_list) != type([]):
        return -1

    
    start = 0
    end = len(input_list) - 1
    output = 0

    if input_list[start] < input_list[end]:

        output = binary_search(input_list,number,start, end)
    else:

        pivot_index = find_pivot(input_list,start, end)

        if number  >= input_list[pivot_index] and number <= input_list[end]:
            output = binary_search(input_list,number,pivot_index, end)
        else:
            output = binary_search(input_list,number,start, pivot_index-1)
    
    return output


def find_pivot(input_list, start,end):
    mid = start  + (end-start) //2
    pivot_index = 0
    if input_list[mid] > input_list[mid+1]:
        return mid +1
    else:
        if input_list[start] > input_list[mid]:
            pivot_index = find_pivot(input_list,start, mid-1)
        else:
            pivot_index = find_pivot(input_list,mid+1, end)
    return pivot_index
        
def binary_search(input_list, target,start,end):
    
    while start <= end:
        mid = (start+end )//2
        if input_list[mid] ==target:
            return mid 
        else:
            if input_list[mid] > target:
            
                end = mid -1
            else:
                start = mid+1
    return -1



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])

test_function([{}, -1])