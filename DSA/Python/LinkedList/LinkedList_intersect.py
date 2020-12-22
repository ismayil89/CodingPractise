'''
LC #
Write a program to find the node at which the intersection of two singly linked lists begins.
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two 
lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as 
[5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the 
intersected node in B.
'''
# Implementation using Hash Table. this has O(N+M) Time and O(N or M) Space complexity
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        
        Ptr_A = headA
        Ptr_B = headB
        Ptr_A_Dict = {}
        
        while Ptr_A:
            Ptr_A_Dict[Ptr_A] = None
            Ptr_A = Ptr_A.next
            
        while Ptr_B:
            if Ptr_B in Ptr_A_Dict:
                return Ptr_B
            Ptr_B = Ptr_B.next
        
        return None
 
 # Implementation using 2 Pointer Concept which has O(N+M) time complexity and O(1) space complexity.
 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        
        Ptr_A = headA
        Ptr_B = headB
        
        while Ptr_A != Ptr_B:
            if not Ptr_A:
                Ptr_A = headB
            else:
                Ptr_A = Ptr_A.next
            
            if not Ptr_B:
                Ptr_B = headA
            else:
                Ptr_B = Ptr_B.next
            
        return Ptr_B       
