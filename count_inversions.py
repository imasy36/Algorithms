## count inversions in an array

def count_inv(arr:list):
	count = 0
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i]>arr[j]:
				count+=1
	return count

if __name__=='__main__':
	arr = [int(x) for x in input('Enter elements: ').split()]
	print("Total inversions: ".format(count_inv(arr)))
