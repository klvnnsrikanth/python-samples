"""
Find the majority element which occurs more than n/2 times in an array of n size, which contains duplicate elements in minimum time and space complexity.
"""

def majority_element(array):
	majority = array[0]
	count = 0
	for elem in array[1:]:
		if elem == majority:
			count += 1
		else:
			count -= 1 
			if count == 0:
				majority = elem
				count += 1
	print majority


majority_element([1,3,4,1,1,7,1])	
