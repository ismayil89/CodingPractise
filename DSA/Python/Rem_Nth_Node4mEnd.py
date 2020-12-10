'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Finding the length of LinkedList and traversing back to remove the element. Requires 2 pass
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or n < 1 or head.next == None:
            return None
        
        count = 0
        itr = head
        while itr:
            count += 1
            itr = itr.next
            
        idx = count - n
        if idx == 0:
            head = head.next
        else:
            count = 1
            itr = head
            while count < idx:
                itr = itr.next
                count += 1
            
            itr.next = itr.next.next
        return(head)
        
        
# Using 2 Pointer Concept. Move the first pointer by N+1 steps and then move both together.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or n < 1 or head.next == None:
            return None
        
        previous = ListNode(None)
        previous.next = head
        Ptr_A = previous
        Ptr_B = previous
        
        # Moving A N+1 steps compared to B
        i = 0
        while i < n+1:
            Ptr_A = Ptr_A.next
            i += 1
        while Ptr_A:
            Ptr_A = Ptr_A.next
            Ptr_B = Ptr_B.next
            
        Ptr_B.next = Ptr_B.next.next
        return(previous.next)
