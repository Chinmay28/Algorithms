import sys


mTable = [[]]
kTable = [[]]
outString = ""

def matrixChainOrder(dim):
    
    # core algorithm as in the book
    n = len(dim)
    for i in range(n):
        mTable[i][i] = 0
        
    for l in range(2, n): # l is the chain-length
        for i in range(1, n-l+1):
        
            j = i+l-1
            # print(i,j)
            mTable[i][j] = float('inf')
            
            for k in range(i, j):
                tableSum = mTable[i][k] + mTable[k+1][j] + dim[i-1] * dim[k] * dim[j]
                if tableSum < mTable[i][j]:
                    mTable[i][j] = tableSum
                    kTable[i][j] = k            
    
    
    
def printParenthesis(i, j):
    
    global outString
    
    if i == j:
        outString += "M" + str(i) +" "

    else:
        k = kTable[i][j]
        outString += "(" + " "
        printParenthesis(i, k)
        outString += "*" + " "
        printParenthesis(k+1, j)
        outString += ")" + " "



"""main()"""
dim = []
n = int(sys.stdin.readline().strip())

for x in range(0, n+1):
    dim.append(int(sys.stdin.readline().strip()))
mTable = [[None for x in range(n+1)] for y in range(n+1)]
kTable = [[None for x in range(n+1)] for y in range(n+1)]

matrixChainOrder(dim)
# print(mTable)
# print(kTable)
printParenthesis(1, n)

# Post process string:
outString = outString.strip()
if outString[0] == "(" and outString[-1] == ")":
    outString = outString[1:len(outString)-1]
# print(kMap)
print(outString.strip())
    
    

