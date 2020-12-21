import math
class PQBinaryHeap:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.pqueue = self.capacity * [None]

    def sizeOf(self):
        return(self.size)

    def isEmpty(self):
        return(self.size == 0)

    def clear(self):
        '''
        Clears the Priority Queue
        '''

    def isLess(self, node1, node2):
        '''
        Compares whethere Node1 is less than Node2
        '''
        return(node1 < node2)

    def addNode(self):
        '''
        Adds the node to Priority Queue
        '''

    def peek(self):
        '''
        Returns the value of element at the Root of Heap (Index - 0)
        '''
        if self.size != 0:
            return(self.pqueue[0])
        
        return(None)
    
    def poll(self):
        '''
        Removes the root of the Heap and returns the value (Index - 0)
        '''

    def remove(self, data):
        '''
        Removes specific value from a Priority Queue
        '''

    def removeAt(self, index):
        '''
        Removes value at a specific Index
        '''

    def sink(self):
        '''
        '''

    def Heapify(self, HeapList):
        # Set current node to last element
        # In Heapify, always start from the last element
        currentNode = len(HeapList) - 1
        while(currentNode > 0):
            parentNode = math.floor((currentNode-1)/2)
            if HeapList[parentNode] < HeapList[currentNode]:
                HeapList[parentNode], HeapList[currentNode] = HeapList[currentNode], HeapList[parentNode]    
                leftChild = 2 * currentNode + 1
                rightChild = 2 * (currentNode + 1)

                if leftChild < len(HeapList): 
                    if rightChild < len(HeapList):
                        if HeapList[leftChild] < HeapList[rightChild]:
                            HeapList[leftChild], HeapList[rightChild] = HeapList[rightChild], HeapList[leftChild]
                    if HeapList[currentNode] < HeapList[leftChild]:
                        HeapList[currentNode], HeapList[leftChild] = HeapList[leftChild], HeapList[currentNode]

            currentNode = currentNode-1

        return(HeapList)
