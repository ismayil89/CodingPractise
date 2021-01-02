__author__ = "Mohamed Ismayil"
__credits__ = ["William Fiset"]
__version__ = "1.0"
__maintainer__ = "Mohamed Ismayil"
__email__ = "ismayil.ece@gmail.com"
__status__ = "Prototype"
__date__ = "19-Dec-2020"

import math

class Node:
    def __init__(self, data, previous, next):
        """
        Constructor: Constructs a Node of Doubly Linked List
        """
        self.data = data
        self.previous = previous
        self.next = next


class DoublyLinkedList:
    """
    Class : DoublyLinkedList
    Description: Pythonic implementation of Doubly Linked List
    """

    def __init__(self):
        """
        Constructor: Declaring head and tail as Null
        """
        self.head = None
        self.tail = None
        self.size = 0

    def clear(self):
        """
        Empties/Clears the Doubly Linked List
        """
        trvs_pointer = self.head
        while trvs_pointer != None:
            nxt_pointer = trvs_pointer.next
            trvs_pointer.previous = trvs_pointer.next = None
            trvs_pointer.data = None
            trvs_pointer = nxt_pointer

        self.head = self.tail = trvs_pointer = None
        self.size = 0

    def getSize(self):
        """
        Returns the size of Doubly Linked List
        """
        return self.size

    def isEmpty(self):
        """
        Validates if the Doubly Linked List is empty?
        """
        return self.size == 0

    def addLast(self, element):
        """
        Inserts the element at the tail of Doubly Linked List
        """
        if self.isEmpty():
            self.head = self.tail = Node(element, None, None)
        else:
            self.tail.next = Node(element, self.tail, None)
            self.tail = self.tail.next

        self.size += 1

    def addFirst(self, element):
        """
        Inserts the element at the head of Doubly Linked List
        """
        if self.isEmpty():
            self.head = self.tail = Node(element, None, None)
        else:
            self.head.previous = Node(element, None, self.head)
            self.head = self.head.previous

        self.size += 1

    def addAt(self, index, data):
        """
        Inserts the element at a specific Index of Doubly Linked List
        """
        if index < 0 or index >= self.size:
            raise Exception("Index out of bound")
        if index == 0:
            self.addFirst(data)
            return True
        elif index == self.size - 1:
            self.addLast(data)
            return True
        else:
            trvs_pointer = self.head

            for iter in range(index):
                trvs_pointer = trvs_pointer.next

            NewNode = Node(data, trvs_pointer.previous, trvs_pointer)
            trvs_pointer.next.previous = NewNode
            trvs_pointer.next = NewNode
            self.size += 1
            return True

    def peekFirst(self):
        """
        Returns the head of Doubly Linked List
        """
        if self.isEmpty():
            raise Exception("List is empty")

        return self.head.data

    def peekLast(self):
        """
        Returns the tail of Doubly Linked List
        """
        if self.isEmpty():
            raise Exception("List is empty")

        return self.tail.data

    def removeFirst(self):
        """
        Removes the head of Doubly Linked List
        """
        if self.isEmpty():
            raise Exception("List is empty")

        data = self.head.data
        self.head = self.head.next
        self.size = self.size - 1

        if self.isEmpty():
            self.tail = None
        else:
            self.head.previous = None

        return data

    def removeLast(self):
        """
        Removes the tail of Doubly Linked List
        """
        if self.isEmpty():
            raise Exception("List is empty")

        data = self.tail.data
        self.tail = self.tail.previous
        self.size = self.size - 1

        if self.isEmpty():
            self.head = None
        else:
            self.tail.next = None

        return data

    def remove(self, node):
        """
        Removes the node from Doubly Linked List
        """
        if node.previous == None:
            return self.removeFirst()
        if node.next == None:
            return self.removeLast()

        node.next.previous = node.previous
        node.previous.next = node.next

        data = node.data
        node.data = node.next = node.previous = None

        self.size = self.size - 1
        return data

    def removeAt(self, index):
        """
        Removes the element at a Specific index of Doubly Linked List
        """
        if index < 0 or index >= self.size:
            raise Exception("Index out of bound")
        if index == 0:
            return self.removeFirst()
        elif index == self.size - 1:
            return self.removeLast()
        else:
            if index < math.ceil(self.size / 2):
                trvs_pointer = self.head
                itr = 0
                while itr < index:
                    trvs_pointer = trvs_pointer.next
                    itr += 1
            else:
                trvs_pointer = self.tail
                itr = self.size - 1
                while itr > index:
                    trvs_pointer = trvs_pointer.previous
                    itr -= 1

            return self.remove(trvs_pointer)

    def valueAt(self, index):
        """
        Returns a value at specific index of Doubly Linked List
        """
        if index < 0 or index >= self.size:
            raise Exception("Index out of bound")
        if index == 0:
            return self.peekFirst()
        elif index == self.size - 1:
            return self.peekLast()
        else:
            if index < math.ceil(self.size / 2):
                trvs_pointer = self.head
                itr = 0
                while itr < index:
                    trvs_pointer = trvs_pointer.next
                    itr += 1
            else:
                trvs_pointer = self.tail
                itr = self.size - 1
                while itr > index:
                    trvs_pointer = trvs_pointer.previous
                    itr -= 1

            return trvs_pointer.data

    def indexOf(self, data):
        """
        Returns the index of specific data in Doubly Linked List
        """
        idx = 0
        trvs_pointer = self.head
        Flag = False
        while idx < self.size:
            # print("OutValue : " + str(trvs_pointer.data))
            if trvs_pointer.data == data:
                # print("INDEX : " + str(idx) + " of " + str(self.size))
                # print("Value : " + str(data))
                # print("Value : " + str(trvs_pointer.data))
                Flag = True
                break
            idx += 1
            trvs_pointer = trvs_pointer.next

        if Flag:
            return idx
        else:
            return False

    def contains(self, data):
        """
        Validates if the value is present in Doubly Linked List
        If it is true, the function returns the index
        """
        return self.indexOf(data)

    def iterator(self):
        """
        Returns the Iterator or Generator Function
        """
        idx = 0
        trvs_pointer = self.head

        while idx < self.size:
            yield trvs_pointer.data
            idx += 1
