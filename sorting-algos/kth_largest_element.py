
# 

arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]

# print(sorted(arr)
# )

def fast_select(arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th lasrgest element in the given array
    

    if k > 0 and k <= len(arr):
        set_of_medians = []
        arr_less_p = []
        arr_equal_p = []
        arr_more_p = []
        i = 0
        
        while i < (len(arr)// 5):
            median = find_median(arr, 5*i, 5)
            set_of_medians.append(median)
            i += 1
            
        
        if 5 * i < len(arr):
            median = find_median(arr, 5*i, len(arr)%5)
            set_of_medians.append(median)
        if len(set_of_medians) == 1:
            pivot = set_of_medians[0]
        elif len(set_of_medians)>1:
            pivot = fast_select(set_of_medians,len(set_of_medians)//2)
            
        for element in arr:
            if element < pivot:
                arr_less_p.append(element)
            elif element > pivot:
                arr_more_p.append(element)
            else:
                arr_equal_p.append(element)

        # print(arr_less_p)
        # print(arr_equal_p)
        # print(arr_more_p)
        
        if k <= len(arr_less_p):
            return fast_select(arr_less_p, k) 
        elif k > (len(arr_less_p) + len(arr_equal_p)):
            return fast_select(arr_more_p, (k-len(arr_less_p)-len(arr_equal_p)))

        else:
            return pivot   
            



def find_median(arr, start, size): 
    my_list = [] 
    for i in range(start, start + size): 
        my_list.append(arr[i]) 
          
    # Sort the array  
    my_list.sort() 
  
    # Return the middle element 
    return my_list[size // 2] 



print(fast_select(arr,10))



