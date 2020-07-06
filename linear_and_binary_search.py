def linear_search(array,element):
	for i in range(len(array)):
		if(array[i] == element):
			return i
	return -1

def binary_search(array,left,right,element):
	if(left<right):
		mid = left + (right-left)//2
		if(array[mid] == element):
			return mid
		elif (element < array[mid]):
			binary_search(array,left,mid-1,element)
		elif (element > array[mid]):
			binary_search(array,mid+1,right,element)
	return -1

my_array = [-2,-1,2,2,3,7,9,14,19,21]
print(linear_search(my_array,3))
print(binary_search(my_array,0,len(my_array)-1,3))