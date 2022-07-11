

def sqrt(num):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if num < 0 :
        return None
    if num == 0:
        return 0
    start = 1
    end = num 
    while start <= end:
        mid = (start+end)//2 
        
        if mid**2 == num:
            return mid 
        elif mid**2 < num:
            start = mid + 1
        else:
            end = mid -1
    return end
    
        

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print("Pass" if (None == sqrt(-25)) else "Fail")
print("Pass" if (None == sqrt(-1)) else "Fail")

