import sys

kMatrix = [[]]
aMatrix = [[]]
pathMatrix = [[]]

def getAdjacencyMatrix(wordList):
    
    aMatrix = [[0 for x in range(n)] for y in range(n)]
    
    for i in range(len(wordList)):
        
        for j in range(len(wordList)):
            if i == j:
                aMatrix[i][j] = 0
            elif aMatrix[j][i] != 0:
                aMatrix[i][j] = aMatrix[j][i]
            else:
                aMatrix[i][j] = getWeight(wordList[i], wordList[j])

    return aMatrix

        
def getWeight(first, second):
    
    flag = False
    weight = 0

    for i in range(len(first)):
        
        if first[i] != second[i] and flag is False:
            flag = True
            weight = abs(ord(second[i]) - ord(first[i]))
            
        elif flag is True and first[i] != second[i]:
            # more than one variable character
            weight = 0
            break            
    
    return weight
            

def floydWarshall(n):
    
    global kMatrix
    global pathMatrix
    
    kMatrix = [[None for x in range(n)] for y in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(i+1):
                if pathMatrix[i][k] + pathMatrix[k][j] < pathMatrix[i][j]:
                    pathMatrix[i][j] = pathMatrix[j][i] = pathMatrix[i][k] + pathMatrix[k][j]
                    kMatrix[i][j] = kMatrix[j][i] = k
                    
               
    statSum = 0     
    for i in range(n):
        for j in range(n):
            if pathMatrix[i][j] != float('inf'):
                statSum += 1
        
    print(round(float(statSum)/n, 2))


# recursive path lookup with k values stored: linear time algorithm
def getPath(path, i, j):
    
    global aMatrix
    global kMatrix
    
    if kMatrix[i][j]:
        path += wordList[i] + " "
        path = getPath(path, kMatrix[i][j], j)
            
    elif aMatrix[i][j] != 0:
        path += wordList[i] + " " + wordList[j] + " "
    
    else:
        path += wordList[i] + " " + wordList[j] + " not reachable"

    return path   
    


"""main()"""

wordList = []
queryList = []

# get the elements
n = int(sys.stdin.readline().strip())
for x in range(n):
    wordList.append(sys.stdin.readline().strip())
    
queryNum = int(sys.stdin.readline().strip())
for x in range(queryNum):
    queryList.append(sys.stdin.readline().strip())
    
aMatrix = getAdjacencyMatrix(wordList)

pathMatrix = [[aMatrix[x][y] for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        if pathMatrix[i][j] == 0 and i != j:
            pathMatrix[i][j] = float('inf')

# Run floyd-warshall algorithm and print the statistic
floydWarshall(n)

for query in queryList:
    tokens = query.split()
    srcIndex = wordList.index(tokens[0])
    dstIndex = wordList.index(tokens[1])
    
    # Get the shortest paths
    outString = ""
    if pathMatrix[srcIndex][dstIndex] != float('inf'):
        outString += str(pathMatrix[srcIndex][dstIndex])
        
    outString += getPath(" ", srcIndex, dstIndex)
    
    print(outString.strip())

    
