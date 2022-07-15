
import re


nums = [1,1,1,1,1]

def runningsum(nums):
    result=[]
    prev_sums=0
    for num in range(0,len(nums)):
       
        if len(result)==0:
            result.append(nums[num])
            prev_sums += nums[num]
            
            continue
        
        next_num = prev_sums + nums[num]
        print(next_num)
        result.append(next_num)
        prev_sums = next_num 
        
    

    return print(result)
runningsum(nums)