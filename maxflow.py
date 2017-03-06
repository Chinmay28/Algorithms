import sys


parentList = []
residualCapacity = {}
currentCapacity = []
weightedEdges = {}
graph = []


def getFlowWithBFS(source, destination):
    
    global parentList
    
    nodeQueue = [source]
    parentList = [None for x in range(len(weightedEdges))]
    parentList[0] = 0 # parent not applicable
    
    # BFS
    while nodeQueue:
        
        currentNode = nodeQueue.pop(0) # front()
        
        for node in weightedEdges[currentNode].keys():
            
            if parentList[node] is None: # not visited yet
                if weightedEdges[currentNode][node] - residualCapacity[currentNode][node] > 0:
                    parentList[node] = currentNode
                    currentCapacity[node] = min(currentCapacity[currentNode],\
                                                weightedEdges[currentNode][node] \
                                                - residualCapacity[currentNode][node])
                    
                    if node == destination:
                        return currentCapacity[node]
                    else:
                        nodeQueue.append(node)
    
    return 0


def edmondKarp(start, end):
    
    global parentList
    
    maxFlow = 0
    
    while True:
        
        flow = getFlowWithBFS(start, end)
#         print(flow)
        if flow == 0:
            break
        
        else:
            maxFlow += flow
            currentNode = end
            
            while currentNode != start:
                previousNode = parentList[currentNode];
                residualCapacity[previousNode][currentNode] += flow;
                residualCapacity[currentNode][previousNode] -= flow;
                currentNode = previousNode;
    
#     print(residualCapacity)
#     print(currentCapacity)
    
    return maxFlow



""" main() """
# number of vertices and edges
[n, m] = sys.stdin.readline().strip().split()
[n, m] = [int(n), int(m)]

# initializations
for x in range(n):
    weightedEdges[x] = {}
    residualCapacity[x] = {}

currentCapacity = [float('inf') for x in range(n)]

# get the capacities
iList = []
jList = []
for x in range(m):
    [i, j, capacity] = sys.stdin.readline().strip().split()
    [i, j, capacity] = [int(i), int(j), int(capacity)]
    weightedEdges[i][j] = capacity
    residualCapacity[i][j] = 0
    residualCapacity[j][i] = 0
    iList.append(i)
    jList.append(j)
    
maxFlow = edmondKarp(0, 1)

# print the flows in the order of input
print(maxFlow)
for i in range(m):
    print(str(iList[i]) + " " + str(jList[i]) + " " + str(residualCapacity[iList[i]][jList[i]]))