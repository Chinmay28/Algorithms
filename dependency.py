import re
import sys


connectedComponents = []

class Graph:
    
    def __init__(self, elementSet):
        
        self.elementSet = elementSet
        self.adjacencyMap = {}
        self.visitRegister = {}
        self.elementStack = []
        self.connectedList = []
        
        for element in elementSet:
            self.adjacencyMap[element] = []
            self.visitRegister[element] = False
    
    
    def addDirectedEdge(self, source, destination):
        # adds an edge between two vertices
        self.adjacencyMap[source].append(destination)
        
        
    def getTranspose(self):
         
        transpose = Graph(self.elementSet)
        
        for source in self.adjacencyMap:
            for destination in self.adjacencyMap[source]:
                transpose.adjacencyMap[destination].append(source)
                
        return transpose
    
    
    def depthFirstSearch(self, element):
        
        # Current element is visited
        self.visitRegister[element] = True
        self.connectedList.append(element)
        
        for destination in self.adjacencyMap[element]:
            if self.visitRegister[destination] is False:
                self.depthFirstSearch(destination)


    def fillElementStack(self, element):
        # another dfs method, only modified to update stack.
        
        # Current element is visited
        self.visitRegister[element] = True
        
        for destination in self.adjacencyMap[element]:
            if self.visitRegister[destination] is False:
                self.fillElementStack(destination)
        
        # All destinations reachable by element are processed.
        # Add element to stack.
        self.elementStack.append(element)
        
 
    def clearVisitRegister(self):
        
        for element in self.elementSet:
            self.visitRegister[element] = False        


    def printStronglyConnectedComponents(self):
        
        # Fill the elementStack according to the corresponding finishing times
        for element in self.elementSet:
            if self.visitRegister[element] is False:
                self.fillElementStack(element)
        
        #print(self.elementStack)

        # Get the transposed graph and clear the visitRegister
        transposedGraph = self.getTranspose()
        self.clearVisitRegister()
        
        # Traverse new graph in the order of Stack entries
        while self.elementStack:
            element = self.elementStack.pop()
            
            if transposedGraph.visitRegister[element] is False:
                transposedGraph.depthFirstSearch(element)
                
                if len(transposedGraph.connectedList) > 1:
                    outString = ""
                    for element in self.elementSet:
                        if element in transposedGraph.connectedList:
                            outString += element
                            outString += " "
                    connectedComponents.append(outString.strip())
                transposedGraph.connectedList = []
        
        # To print components in the right order
        # Some sorting. Sadly it is n^2 :-(
        for element in self.elementSet:
            for componentString in connectedComponents:
                matchList = re.findall("\\b"+element+"\\b", componentString)
                if matchList:
                    print(componentString)
                    connectedComponents.remove(componentString)
                    continue
                
        


"""main()"""

# print(g.adjacencyMap)
elementSet = []
# get the elements
n = int(sys.stdin.readline().strip())
for x in range(n):
    elementSet.append(sys.stdin.readline().strip())
    
# get directed edges
n = int(sys.stdin.readline())
graph1 = Graph(elementSet)

for i in range(n):
    link = sys.stdin.readline().strip()
    tokens = link.split(" ")
    graph1.addDirectedEdge(tokens[0], tokens[1])

graph1.printStronglyConnectedComponents()