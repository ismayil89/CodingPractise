class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index == 0:
            return self.head.data
        else:
            itr = self.getNextIndex(index + 1)
            return itr.data

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val, self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            node = Node(val, self.head)
            self.head = node

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        print("Adding value {0} at the index {1}".format(val, index))
        if index == 0:
            self.addAtHead(val)
        elif index == self.getLenOfLinkedList():
            self.addAtTail(val)
        else:
            print("Index is " + str(index))
            itr = self.getNextIndex(index)
            itr.next = Node(val, itr.next)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        print("Deleting value at the index {0}".format(index))
        if index == 0:
            self.head = self.head.next
        else:
            itr = self.getNextIndex(index)
            itr.next = itr.next.next

    def getNextIndex(self, index: int) -> object:
        """
        Returns the Memory location of specified Index
        """
        if index > self.getLenOfLinkedList():
            raise Exception("Index out of Range")

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                break
            count += 1
            itr = itr.next

        return itr

    def getLenOfLinkedList(self):
        """
        Returns the Length of Linked List
        """
        itr = self.head
        count = 1
        while itr.next:
            count += 1
            itr = itr.next
        print("Length of LL : " + str(count))
        return count

    def printLinkedList(self):
        if self.head is None:
            print("Invalid")
            return

        itr = self.head
        lnkList = ""
        while itr:
            lnkList += str(itr.data) + "--->"
            itr = itr.next

        print(lnkList)


if __name__ == "__main__":
    # Your SinglyLinkedList object will be instantiated and called as such:
    obj = SinglyLinkedList()
    # param_1 = obj.get(index)
    obj.addAtHead(5)
    obj.addAtHead(15)
    obj.addAtHead(25)
    obj.printLinkedList()
    obj.addAtTail(20)
    obj.printLinkedList()
    obj.addAtIndex(2, 99)
    obj.printLinkedList()
    print("Deleting")
    obj.deleteAtIndex(3)
    obj.printLinkedList()
    param_1 = obj.get(3)
    print(param_1)
