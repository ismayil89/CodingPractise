'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        while head and head.val == val:
            head = head.next
        
        Current_Ptr = head
        if head:
            Next_ptr = head.next
        else:
            return Current_Ptr
        while Next_ptr:
            if Next_ptr.val == val:
                Current_Ptr.next = Current_Ptr.next.next
                if Next_ptr == None:
                    break
            else:
                Current_Ptr = Current_Ptr.next
            Next_ptr = Next_ptr.next
                
        return head
