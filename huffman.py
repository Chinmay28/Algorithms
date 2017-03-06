import sys
 

class Node:
    # Node for Huffman tree
    
    def __init__(self, item=None, frequency=0):
        self.item = item
        self.frequency = frequency
        self.left = None
        self.right = None

 
class TrinaryHeap:
 
    def __init__(self, nodeList):
         
        self.trinaryHeap = []
        for node in nodeList:
            self.insert(node)
         
     
    def getParent(self, index):
         
        if index == 0:
            # You are at root!
            return None
        else:
            return int((index-1)/3)
         
         
    def getFirst(self, index):
         
        if (index*3 + 1) >= len(self.trinaryHeap):
            return None
        else:
            return index*3 + 1
     
     
    def getSecond(self, index):
         
        if (index*3 + 2) >= len(self.trinaryHeap):
            return None
        else:
            return index*3 + 2
         
         
    def getThird(self, index):
         
        if (index*3 + 3) >= len(self.trinaryHeap):
            return None
        else:
            return index*3 + 3
         
     
    def minHeapify(self, index):
     
        first = self.getFirst(index)
        if first is None:
            # leaf node
            return self.trinaryHeap
             
        second = self.getSecond(index)
        third = self.getThird(index)
         
        # map to avoid index() call that's ineffective 'coz of duplicates
        index_map = {}
        index_map[self.trinaryHeap[first].frequency] = first
        if second:
            index_map[self.trinaryHeap[second].frequency] = second
        if third:
            index_map[self.trinaryHeap[third].frequency] = third
         
        # core logic
        smallest = first
        if second and not third:
            smallest = index_map[min(self.trinaryHeap[first].frequency, \
                                     self.trinaryHeap[second].frequency)]    
         
        if first and second and third:
            smallest = index_map[min(self.trinaryHeap[first].frequency, \
                                     self.trinaryHeap[second].frequency, \
                                     self.trinaryHeap[third].frequency)]
         
        #print(smallest)
        if self.trinaryHeap[smallest].frequency < self.trinaryHeap[index].frequency:
            # swap
            self.trinaryHeap[smallest], self.trinaryHeap[index] = \
            self.trinaryHeap[index], self.trinaryHeap[smallest]
         
        #     print(trinaryHeap, index)
        self.minHeapify(smallest)
     
     
    def extractMin(self):
        # extract the minimum and do a minHeapify()
        value = self.trinaryHeap[0]
        self.trinaryHeap[0] = self.trinaryHeap[-1]
        self.trinaryHeap = self.trinaryHeap[:-1]
        self.minHeapify(0)
        
        return value
     
     
    def insert(self, node):
        # insert at the end of the tree and percolateUp()
        self.trinaryHeap.append(node)
        self.percolateUp(len(self.trinaryHeap)-1)
     
 
    def percolateUp(self, index):
         
        parent = self.getParent(index)
        if parent is None:
            return self.trinaryHeap
     
        else:
            if self.trinaryHeap[index].frequency < self.trinaryHeap[parent].frequency:
                # swap
                self.trinaryHeap[index], self.trinaryHeap[parent] = \
                self.trinaryHeap[parent], self.trinaryHeap[index]
             
        self.percolateUp(parent)
 
 
 
class Huffman:
     
    def __init__(self, inputData):
         
        self.freqMap = {}
        self.pQueue = None
        self.codeMap = {}
        
        # initialize freqMap
        for x in range(0,256):
            self.freqMap[x] = 1
        
        self.freqMap["EOF"] = 1
        
        index = 0
        
        # parse the inputData and update frequencies
        while index < len(inputData):
            self.freqMap[ord(inputData[index])] += 1
            index += 1    
#         print(self.freqMap)  


    def makePriorityQueue(self):
        
        nodeList = []
        for key in self.freqMap:
            node = Node(item=key, frequency=self.freqMap[key])
            nodeList.append(node)
        
        self.pQueue = TrinaryHeap(nodeList)
        
    
    def generateCode(self):
        
        # core huffman code algorithm as in the book
        n = len(self.pQueue.trinaryHeap)
        for x in range(1,n):
            node = Node()
            node.left = self.pQueue.extractMin()
            node.right = self.pQueue.extractMin()
            node.frequency = node.left.frequency + node.right.frequency
#             print(node.item, node.frequency)
            self.pQueue.insert(node)
        
        root = self.pQueue.extractMin()
        self.collectCode(root, "")
        
        # print the code for each key
        for key in range(1,256):
            if key in range(33, 127):
                print(chr(key) + ": " + self.codeMap[key])
            else:
                print('{:02x}'.format(key).upper() + ": " + self.codeMap[key])
        
        # print EOF's code as well in the end.
        print("EOF: " + self.codeMap["EOF"])
        
        
    def collectCode(self, node, code):
        # traverse the huffman tree and collect code for each key
        
        if node.left is None and node.right is None:
            self.codeMap[node.item] = code
        
        else:
            if node.left:
                self.collectCode(node.left, code + "0")
            if node.right:
                self.collectCode(node.right, code + "1")
            
            
        
""""main()"""

inputData = sys.stdin.read()

h = Huffman(inputData)
h.makePriorityQueue()
h.generateCode()    