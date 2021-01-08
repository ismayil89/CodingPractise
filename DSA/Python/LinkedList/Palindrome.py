import SinglyLinkedList as SLL
class ListNode:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next

class Palindrome:
    def __init__(self):
        pass

    def isPalindrome(self, head) -> bool:
        if head == None or head.next == None:
            return True
        Ptr_A = Ptr_B = Ptr_D = head
        Ptr_D = self.copy_list(Ptr_D)
    
        mid = None
        while Ptr_B.next:
            if Ptr_B.next.next:
                Ptr_A = Ptr_A.next
                Ptr_B = Ptr_B.next.next
            else:
                break
            
        mid = Ptr_A
        Ptr_B = head
        Ptr_B = self.reverseList(Ptr_B)
        while(Ptr_B != mid):
            if Ptr_D.data == Ptr_B.data:
                Ptr_D = Ptr_D.next
                Ptr_B = Ptr_B.next
                
            else:
                return False
        return True

    def copy_list(self, head):
        if head is None:
            return head

        # Create a new node
        new_node = ListNode(head.data)
        # The new nodes next pointer would point to the node returned from recursion
        # i.e. the next new node.
        new_node.next = self.copy_list(head.next)

        return new_node

    def reverseList(self, head):
        Ptr_previous = None
        Ptr_current = head
        while Ptr_current:
            Ptr_next = Ptr_current.next
            Ptr_current.next = Ptr_previous
            Ptr_previous = Ptr_current
            Ptr_current = Ptr_next

        return Ptr_previous

if __name__ == "__main__":
    # Your SinglyLinkedList object will be instantiated and called as such:
    obj = SLL.SinglyLinkedList()
    obj.addAtTail(1)
    obj.addAtTail(0)
    obj.addAtTail(1)
    obj.addAtTail(1)
    print(f"\nOriginal Linked List:")
    obj.printLinkedList()
    
    myLL = obj.getLinkedList()
    Pobj = Palindrome()
    print(Pobj.isPalindrome(myLL))