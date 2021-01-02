__author__ = "Mohamed Ismayil"
__credits__ = ["William Fiset"]
__version__ = "1.0"
__maintainer__ = "Mohamed Ismayil"
__email__ = "ismayil.ece@gmail.com"
__status__ = "Prototype"
__date__ = "23-Dec-2020"

import math
class PQBinaryHeap:
    def __init__(self, ascendig=True):
        self.size = 0
        self.capacity = 10
        self.ascending = ascendig
        self.pqueue = self.capacity * [None]
        self.dataType = None

    def sizeOf(self):
        '''
        Returns the size of Priority Queue
        '''
        return(self.size)

    def isEmpty(self):
        '''
        Validates if the priority Queue is empty
        '''
        return(self.sizeOf() == 0)

    def clear(self):
        '''
        Clears the Priority Queue
        '''
        self.pqueue = []
        self.size = 0
        return(self.sizeOf())

    def addNode(self, data):
        '''
        Adds the node to Priority Queue
        '''
        if self.sizeOf == 10:
            raise Exception(f'Priority Queue is Full')

        if self.sizeOf() == 0:
            self.dataType = type(data)

        if self.dataType != type(data):
            raise Exception(f'Data of type {type(data)} can\'t be combined with {type(self.dataType)}')

        self.pqueue[self.size] = data
        self.size += 1
        if self.sizeOf() > 1:
            if self.ascending:
                self.MinHeap()
            else:
                self.MaxHeap()

        return(self.sizeOf())

    def peek(self):
        '''
        Returns the value of element at the Root of Heap (Index - 0)
        '''
        if self.sizeOf() != 0:
            return(self.pqueue[0])
        
        return(None)
    
    def poll(self):
        '''
        Removes the root of the Heap and returns the value (Index - 0)
        '''
        if self.sizeOf() > 1:
            if self.ascending:
                self.MinHeap()
            else:
                self.MaxHeap()

        if self.sizeOf() > 0:
            data = self.pqueue[0]
            self.pqueue[0] = self.pqueue[self.size-1]
            self.pqueue[self.size-1] = None
            self.size -= 1
            return(data)
        
        return(None)

    def contains(self,data):
        '''
        Returns True/False if the element is present in Priority Queue
        '''
        if data in self.pqueue:
            return(True)
        else:
            return(False)

    def MaxHeap(self):
        '''
        This function returns the Max Heap of current Priority List
        '''
        # Set current node to last element
        # In Heapify, always start from the last element
        #print(25 * '#')
        #print("Size is " + str(self.sizeOf()))
        cN = self.sizeOf() - 1 # Current Node
        #print(self.pqueue[cN])
        while(cN > 0):
            pN = math.floor((cN - 1)/2) # Parent Node
            if self.pqueue[pN] < self.pqueue[cN]:
                self.pqueue[pN], self.pqueue[cN] = self.pqueue[cN], self.pqueue[pN]    
                lC = 2 * cN + 1 # Left Child
                rC = 2 * (cN + 1) # Right Child

                if lC < self.sizeOf(): 
                    if rC < self.sizeOf():
                        if self.pqueue[lC] < self.pqueue[rC]:
                            self.pqueue[lC], self.pqueue[rC] = self.pqueue[rC], self.pqueue[lC]
                    if self.pqueue[cN] < self.pqueue[lC]:
                        self.pqueue[cN], self.pqueue[lC] = self.pqueue[lC], self.pqueue[cN]

            cN = cN - 1

    def MinHeap(self):
        '''
        This function returns the Min Heap of current Priority List
        '''
        # Set current node to last element
        # In Heapify, always start from the last element
        cN = self.sizeOf() - 1 # Current Node
        while(cN > 0):
            pN = math.floor((cN - 1)/2) # Parent Node
            if self.pqueue[pN] > self.pqueue[cN]:
                self.pqueue[pN], self.pqueue[cN] = self.pqueue[cN], self.pqueue[pN]    
                lC = 2 * cN + 1 # Left Child
                rC = 2 * (cN + 1) # Right Child

                if lC < self.sizeOf(): 
                    if rC < self.sizeOf():
                        if self.pqueue[lC] > self.pqueue[rC]:
                            self.pqueue[lC], self.pqueue[rC] = self.pqueue[rC], self.pqueue[lC]
                    if self.pqueue[cN] > self.pqueue[lC]:
                        self.pqueue[cN], self.pqueue[lC] = self.pqueue[lC], self.pqueue[cN]

            cN = cN - 1
