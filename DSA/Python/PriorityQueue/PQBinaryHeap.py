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
