#subset sum problem

def ssp(arr, w):
    rows, cols = len(arr)+1, w+1
    mat=[[0 for x in range(cols)]for y in range(rows)]

    for i in range(rows):
        mat[i][0] = True
        
    for j in range(1,cols):
        mat[0][j] = False

    for i in range(1,rows):
        for j in range(1,cols):
            if arr[i-1]>j:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j-arr[i-1]] or mat[i-1][j]

    # getting subset if possible            
    if mat[-1][-1]:
        subset, i, j = [], rows-1, cols-1
        while j>-1 and i>0:
            if mat[i-1][j]==False:
                subset.append(arr[i-1])
                j-=arr[i-1]
            i-=1
        return [ mat[-1][-1], subset ]

    # If subset not possible
    else:
        return [ mat[-1][-1], None ]
    
if __name__=='__main__':
    arr = list(map(int, input("Enter array elements : ").split()))
    w = int(input("Enter sum value: "))
    ans = ssp(arr, w)
    print("subset {}".format("Possible  || subset = {}".format(ans[1]) if ans[0] else "Not Possible"))
