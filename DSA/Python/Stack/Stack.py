class Node:
    '''
    Class to create a Node
    '''
    def __init__(self,data=None, next=None) -> None:
        self.data = data
        self.next = next

class Stack:
    '''
    Stack Implementation using Singly Linked List
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
    
    def sizeOf(self):
        '''
        Returns the Size of Stack
        '''
        return(self.size)

    def push(self, val: int) -> None:
        '''
        Pushes the Element to the Top of the Stack (Head of Linked List)
        '''
        node = Node(val,self.head)
        self.head = node
        self.size += 1
        return(self.size)   

    def pop(self):
        '''
        Pops the Element from the Top of the Stack 
        '''
        if self.head is None:
            raise Exception("Stack is Empty")
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return(data)

    def peek(self):
        '''
        Returns the Element at the Top of the Stack
        '''
        if self.head is None:
            raise Exception("Stack is Empty")
        return(self.head.data)

    def search(self, data):
        '''
        Search and return the index of element in a Stack
        '''
        if self.head is None:
            raise Exception("Stack is Empty")

        trvs_pointer = self.head
        index = 0

        while index < self.size:
            if trvs_pointer.data == data:
                return index

            index += 1
            trvs_pointer = trvs_pointer.next
        
        return False

    def clear(self):
        '''
        Clears the content of Stack
        '''
        if self.size > 0:
            while(self.size != 0):
                self.pop()
                
        return(self.sizeOf() == 0)