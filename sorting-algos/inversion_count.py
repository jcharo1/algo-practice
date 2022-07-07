
def count_inversions(arr):
    
    start_index = 0
    end_index = len(arr)-1
    output = inversion_count(arr,start_index,end_index)
    return output
def inversion_count(arr, start_index,end_index):
    if start_index >= end_index:
    
        return 0
    
    
    
    mid_index = start_index + (end_index - start_index)//2
    left_answer = inversion_count(arr,start_index,mid_index)
    right_answer = inversion_count(arr,mid_index +1,end_index)
    

    output = left_answer + right_answer
    
    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    return output



def  merge_two_sorted_halves():
d=[7, 5, 3, 1]
count_inversions(d)





252950

