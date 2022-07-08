test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
def sort_012(input_list):
    """
    The idea is to put 0 and 2 in their correct positions, which will make sure
    all the 1s are automatically placed in their right positions
    """
    # initialize pointers for next positions of 0 and 2
    next_post_0 = 0
    next_post_2 = len(input_list) -1 

    front_index = 0

    while front_index <= next_post_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_post_0]
            input_list[next_post_0] = 0
            next_post_0 += 1
            front_index +=1
            return input_list
        elif input_list[front_index] == 2 :
            input_list[front_index] = input_list[next_post_2]
            input_list[next_post_2] = 2 
            next_post_2 -= 1 
            return input_list
        else:
            front_index += 1
            return input_list

print(sort_012(test_case)
)