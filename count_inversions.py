## counting inversions in an array

def count_inv(arr:list):
	count = 0
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i]>arr[j]:
				count+=1
	return count


def mergeAndCountInv(b:list, c:list):
	result = []
	count  = 0 
	l = len(b) + len(c)
	i=j=k=0
	while i<len(b) and j<len(c):
		if b[i]<c[j]:
			result.append(b[i])
			i+=1
		else:
			result.append(c[j])
			j+=1
			if k<l//2:
				count+= len(b) - i
		k+=1

	while i<len(b):
		result.append(b[i])
		i+=1
		k+=1
	
	while j<len(c):
		result.append(c[j])
		j+=1
		k+=1

	return result, count


def countAndSortInv(arr:list):
	if len(arr)==1:
		return [arr, 0]
	n = len(arr)
	b, count_b = countAndSortInv(arr[:n//2])
	c, count_c = countAndSortInv(arr[n//2:])
	d, count_d = mergeAndCountInv(b, c)

	## print(d," - ",count_b + count_c + count_d)
	return [d, count_b + count_c + count_d]


if __name__=='__main__':
	arr = [int(x) for x in input('Enter elements: ').split()]
	print("Total inversions: {}  --O(n^2)".format(count_inv(arr)))
	print("Total inversions: {}  --O(nlogn)".format(countAndSortInv(arr)[1]))
	