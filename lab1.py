# Name: Arti Jain         
# Course: CPE 202
# Instructor: Hatalsky 
# Assignment: Lab 1 Part 1
# Term: Spring 2019

# must use iteration not recursion
# finds the max of a list of numbers and returns the value (not the index)
# If int_list is empty, returns None. If list is None, raises ValueError
def max_list_iter(int_list):  
    if int_list == None: 			
        raise ValueError("empty list")	# if the list is empty, raise error
    elif int_list == []:
    	return None
   						 				# uses for loop for iteration and takes the max value
    high = int_list[0]   				# high is the max value and starts as the first value in list
    for count in range(len(int_list)):
        if high < int_list[count]: 		# if the current value in high is less than the 
            high = int_list[count] 		# current value in the list, update high
    return high


# must use recursion
# recursively reverses a list of numbers and returns the reversed list
# If list is None, raises ValueError

def reverse_rec(int_list): 
    if int_list == None:                # if the list is None, raise error
        raise ValueError("empty list")
    if len(int_list) == 0:				# if the list is empty, return []
    	return []
    elif len(int_list) == 1:			# if the list is one value, return that one value [value]
    	return [int_list[0]]
    else:
    	return reverse_rec(int_list[1:]) + [int_list[0]] # putting the first value at the end
														 # calling the recursive function on the 
														 # first part of the list until last value is 
        												 # at the front


 # must use recursion
 # searches for target in int_list[low..high] and returns index if found
 # If target is not found returns None. If list is None, raises ValueError 
def bin_search(target, low, high, int_list):
    if int_list == None:
    	raise ValueError("empty list")
    if int_list == []:
        return None
    if len(int_list) == 1:
        if target == int_list[low]:
            return low
        else:
        	return None
    if low > high:
    	return None
    while low <= high:
        middle = (high + low) // 2
        if target == int_list[middle]:
            return middle
        elif target < int_list[middle]:
            return bin_search(target, low, (middle-1), int_list)
        elif target > int_list[middle]:
            return bin_search(target, (middle+1), high, int_list)
