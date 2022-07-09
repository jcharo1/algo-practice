def maxSubArray(arr):
    '''
    param: An array `arr`
    return: The maximum sum of the contiguous subarray. 
    No need to return the subarray itself.
    '''
    start= 0
    stop = len(arr)-1
    return max_sub_array_recursive(arr,start,stop)

def max_crossing_sum(arr,start,mid,stop):
    left_sum = arr[mid]
    left_max_sum = arr[mid]

    for i in range(mid-1,start-1,-1):
        left_sum= left_sum + arr[i]
        if left_sum > left_max_sum:
            left_max_sum = left_sum

    right_sum = arr[mid+1]
    right_max_sum = arr[mid+1]

    for j in range(mid+2, stop+1):
        right_sum = right_sum + arr[j]
        if right_sum > right_max_sum:
            right_max_sum = right_sum
    
    return (right_max_sum +left_max_sum)

def max_sub_array_recursive(arr,start,stop):
    if start == stop:
        return arr[start]

    if start<stop:
        mid = (start+stop)//2
        left = max_sub_array_recursive(arr,start,mid)
        right = max_sub_array_recursive(arr, mid+1, stop)
        center = max_crossing_sum(arr,start,mid,stop)
        return max(center,max(left,right))

    else:
        return arr[start]




# Test your code
arr = [-2, 7, -6, 3, 1, -4, 5, 7] 
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 13