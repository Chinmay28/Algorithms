

kMap = {}
table = [[]]
outString = ""

def matrixChainOrder(dim, i, j):
    
    if i == j:
        table[i][j] = 0
        return 0
    
    elif table[i][j]:
        return table[i][j]

    else:
        minValue = float('inf')
        for k in range(i, j):
            value = matrixChainOrder(dim, i, k) + matrixChainOrder(dim, k+1, j) + dim[i-1] * dim[k] * dim[j]
            if value < minValue:
                minValue = value
                kMap[str(i)+","+str(j)] = k
        # print (i, j, k, minValue)
        table[i][j] = minValue
        # print(table)
        return table[i][j]
    
    
def printParenthesis(i, j):
    
    global outString
    
    if i == j:
        outString += "M" + str(i) +" "

        if i != n:
            outString += "*" + " "

    else:
        k = kMap[str(i)+","+str(j)]
        outString += "(" + " "
        printParenthesis(i, k)
        #put star here
        printParenthesis(k+1, j)
        outString += ")" + " "



"""main()"""
dim = []
n = int(input('').strip())

for x in range(0, n+1):
    dim.append(int(input('').strip()))
table = [[None for x in range(n+1)] for y in range(n+1)] 

matrixChainOrder(dim, 1, n)
# print(kMap)
printParenthesis(1, n)
#print(outString.strip())

# Post process string:
outString = outString.replace("* )", ")")
outString = outString.replace(") M", ") * M")
outString = outString.replace(") (", ") * (")
outString = outString.strip()

if outString[0] == "(" and outString[-1] == ")":
    outString = outString[1:len(outString)-1]
# print(kMap)
print(outString.strip())
    
    

