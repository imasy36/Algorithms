#merge_sort

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left, right = arr[:mid], arr[mid:]
        merge_sort(left)
        merge_sort(right)
        #conquer
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i+=1
            else :
                arr[k] = right[j]
                j+=1
            k+=1
            
        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
            
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        return arr    

if __name__=='__main__':
    data = map(int,input("Enter array elements: ").split())
    data = list(data)
    data = merge_sort(data)
    print("Sorted data: ",end="")
    for x in data:
        print(x,end=", ")
