# 0 1 knapsack problem

def knapsack(W, w, v):
    row, col = len(w)+1, W+1 
    mat= [[0 for j in range(col)]for i in range(row)]

    for i in range(1,row):
        for j in range(1,col):
            temp = j - w[i-1]
            if temp<0:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = max(mat[i-1][j], v[i-1]+mat[i-1][j-w[i-1]])
    return mat[-1][-1]

if __name__=='__main__':
    weights = list(map(int, input("Enter weights : ").split()))
    costs = list(map(int, input("Enter costs : ").split()))
    W = int(input("Enter max weigth : "))
    items = [x for x in range(1,len(weights)+1)]
    print("-----------------------------\nItems || Weights || Profits")
    for x in items:
        print("   {}  ||    {}   ||  {}  ".format(x, weights[x-1], costs[x-1]))
    print("-----------------------------")
    print("Max Profit is: {} ".format(knapsack(W,weights, costs)))
