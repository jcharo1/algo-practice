
import sys 


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return (None, None)
    if len(ints) == 1:
        return (ints[0],ints[0])
    max = -float('inf')
    min = float('inf')

    for num in ints:
        if num < min:
            min = num
        if num > max:
            max = num
   
    return (min,max) 

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
l=[9, 7, 4, 8, 0, 3, 5, 2, 1, 6]


print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((2, 2) == get_min_max([2])) else "Fail")
print("Pass" if ((-1, 1) == get_min_max([1, -1])) else "Fail")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")
