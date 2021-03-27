## merge sort 
def merge(left:list, right:list)->list:
	i,j=0,0
	result = []
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1

	while i<len(left):
		result.append(left[i])
		i+=1

	while j<len(right):
		result.append(right[j])
		j+=1

	return result

def merge_sort(arr:list)->list:	
	length = len(arr)
	## base case
	if length==1:
		return arr
	## recursive calls
	left = merge_sort(arr[:length//2])
	right = merge_sort(arr[length//2:])

	## merging arrays
	return merge(left, right)


if __name__=='__main__':
	array = [int(x) for x in input().split()]
	print("Sorted array : {}".format(merge_sort(array)))
