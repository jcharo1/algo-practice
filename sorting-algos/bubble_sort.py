
# Bubble Sort Exercises  ===================

# Exercise 1
# Sam records when they wake up every morning. Assuming Sam always wakes up in the same hour, use bubble sort to sort by earliest to latest.

from time import sleep


# wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
# def bubble_sort_1(unsorted_array):
#     # TODO: Implement bubble sort solution


#     # len(wakeup_times) == 19  range(len(wakeuptimes)) range-----0,18
#     # range(1,len(wakeup_times)) --   1-18
#     for iteration in range(len(unsorted_array)):
#         # print(f"{iteration}-------------------------------------ITERATION-----------------------------------------------------------------------")
        
#         for index in range(1,len(wakeup_times)):
#             current_element= unsorted_array[index]
#             previous_element = unsorted_array[index-1]
#             # print(f"{index}======== Index ")
#             # print(f"{current_element}======== Current element")
#             # print(f"{previous_element}======== previous element")
            
            
#             if previous_element <= current_element:
#                 continue

#             unsorted_array[index] = previous_element
#             unsorted_array[index - 1] = current_element
            
        
    


# print ("Pass" if (wakeup_times[0] == 3) else "Fail")





# Exercise 2

# Sam doesn't always go to sleep in the same hour. Given the following times Sam has gone to sleep, sort the times from latest to earliest.

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13),(21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(unsorted_array):
    for times in range(len(unsorted_array)):

        for index in range(1,len(unsorted_array)):
            current_element = unsorted_array[index]
            prev_element = unsorted_array[index-1]
            if prev_element>= current_element:
                continue   

            unsorted_array[index-1]= current_element
            unsorted_array[index]= prev_element

bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")

