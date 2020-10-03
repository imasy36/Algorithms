# matrix chain multiplication
# author @imasy36
import sys
import re
class matrix:
    '''
    Class to store matrix data with following functions:
    shape : return shape of matrix as tuple
    __str__ : for print function
    __mul__ : overloading multiplication operator
    '''
    def __init__(self, mat):
        self.matrix = mat
        self.n = len(mat)
        self.m = len(mat[0])
        
    def shape(self):
        return (self.n, self.m)

    def __str__(self):
        res = "Matrix : \n"
        for x in self.matrix:
            for y in x:
                res+=str(y) + "  "
            res+="\n"
        return res   

    def __mul__(self, ob):
        if self.m!=ob.n:
            print("Multiplication not possible")
            return None
        result = [[0 for x in range(ob.m)]for y in range(self.n)]
        for i in range(self.n):
            for j in range(ob.m):
                for k in range(self.m):
                    result[i][j]+=self.matrix[i][k]*ob.matrix[k][j] 
        return matrix(result)

class MCM:
    '''
    MCM class with following functions
    mcm_order : to caculate the order in which matrices should be multiplied so that minimum multiplication operation occurs
    mcm : to generate m and s matrix 
    get_order : return order
    min_cost : return minimum cost of matrix multiplication
    '''
    def __init__(self, p, no=65):
        self.no = no
        self.mm, self.sm = self.mcm(p) #s matrix and m matrix
        self.order=""
        self.mcm_order(self.sm, 1, len(self.sm[0])-1)
        
    def mcm_order(self, s, i, j):
        if i==j:
            self.order+=chr(self.no)
            self.no+=1
            return
        self.order+='('
        self.mcm_order(s, i, s[i][j])
        self.mcm_order(s, s[i][j]+1, j)
        self.order+=')'
        return

    def mcm(self, p):
        n = len(p)
        res = [[0 for x in range(n)]for y in range(n)]
        s= [[0 for x in range(n)]for y in range(n)]
        for l in range(2,n):
            for i in range(1,n-l+1):
                j =i+l-1
                res[i][j]=sys.maxsize
                for k in range(i,j):
                    q = res[i][k] + res[k+1][j] + p[i-1]*p[j]*p[k]
                    if q<res[i][j]:
                        res[i][j]=q
                        s[i][j]=k
        return res, s

    def shape(self):
        return "M_matirx: ({}, {}) | S_matrix: ({}, {})".format(len(self.mm), len(self.mm[0]), len(self.sm), len(self.sm[0]))

    def min_cost(self):
        return self.mm[1][-1]

    def get_order(self):
        return self.order

def output(matrices, order):
    # yet to complete
    '''
    input = matrices ex-{'A': matrix  . . ..} , order string ex- (A((BC)D))
    output = result martix after multiplication
    '''
    return 0

if __name__=='__main__':
    print("Enter no of Matrices")
    n = int(input())
    matrices = {}
    p = []
    alph = ['A','B','C','D','E','F']
    for _ in range(n):
        inp = []
        while True:
            temp = input().split()
            if temp[0].lower()=="done":
                break
            else:
                inp.append([int(x) for x in temp])       
        matrices[alph[_]] = matrix(inp)
        p.append(len(inp))
    p.append(len(inp[0]))
    print("-------------------------")
    for k in matrices:
        print("{} : ".format(k))
        print(matrices[k])
    var_mcm = MCM(p)
    print("Min cost is: ", var_mcm.min_cost() )
    order =  var_mcm.get_order() 
    print("Order : ",order)
    print(output(matrices, order))        
