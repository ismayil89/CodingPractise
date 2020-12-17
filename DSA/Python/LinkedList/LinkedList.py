class Node:
    def __init__(self, data, previous, next):
        self.data = data
        self.previous = previous
        self.next = next
        
class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.size = 0

    def clear(self):
        trvs_pointer = self.head

        while trvs_pointer != None:
            nxt_pointer = trvs_pointer.next
            trvs_pointer.previous = trvs_pointer.next = None
            trvs_pointer.data = None
            trvs_pointer = nxt_pointer

        self.head = self.tail = trvs_pointer = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return(self.size == 0)
    
    def addLast(self, element):
        if self.isEmpty():
            self.head = self.tail = Node(element, None, None)
        else:
            self.tail.next =  Node(element, self.tail, None)
            self.tail = self.tail.next

        self.size += 1 

    def addFirst(self, element):
        if self.isEmpty():
            self.head = self.tail = Node(element, None, None)
        else:
            old_pointer = self.head
            self.head.previous =  Node(element, None, self.head)
            self.head = self.head.previous

        self.size += 1 

    def addAt(self, index, data):
        if index < 0 or index > self.size:
            raise Exception("Index out of bound")
        if index == 0:
           self.addFirst(data)
           return True
        elif index == self.size:
            self.addLast(data)
            return True
        else:
            trvs_pointer = self.head

            for iter in range(index):
                trvs_pointer = trvs_pointer.next
            
            NewNode = Node(data, trvs_pointer.previous, trvs_pointer)
            trvs_pointer.next.previous = NewNode
            trvs_pointer.next =  NewNode
            self.size += 1
            return True

    def peekFirst(self):
        if self.isEmpty:
            raise Exception("List is empty")

        return self.head.data

    def peekLast(self):
        if self.isEmpty:
            raise Exception("List is empty")

        return self.tail.data
            