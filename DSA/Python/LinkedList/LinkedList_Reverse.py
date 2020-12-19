"""
LC #206 
Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Iterative Method

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        Ptr_previous = None
        Ptr_current = head
        while Ptr_current:
            Ptr_next = Ptr_current.next
            Ptr_current.next = Ptr_previous
            Ptr_previous = Ptr_current
            Ptr_current = Ptr_next

        return Ptr_previous
