def partition(arr, p, r): 
    i = p - 1		
    pivot = arr[r]	 
    for j in range(p, r):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[r] = arr[r],arr[i+1] 
    return i+1 

def quicksort(arr, p, r): 
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, q+1, r)
    return arr

if __name__=='__main__':
    arr = list(map(int, input("Enter elements: ").split()))
    print("Initial Array is: ",arr)
    arr = quicksort(arr, 0, len(arr)-1)
    print("Sorted  Array is: ",arr)
