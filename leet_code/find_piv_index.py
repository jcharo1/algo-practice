from turtle import right


nums = [1,7,3,6,5,6]

sum_of_nums = sum(nums)
left_sums= 0 
for index,num in enumerate(nums):
    print(index,num)
    current_num= num 
    right_sums= sum_of_nums - current_num
    print(right_sums)

