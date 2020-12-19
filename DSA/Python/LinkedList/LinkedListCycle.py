"""
LC - #
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the 
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        count = 0
        Flag = False
        while head:
            head = head.next
            if count > 10000:
                Flag = True
                break
            count += 1

        return Flag


# With Two pointer concept where one pointer steps twice the other


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False

        single_step = head
        double_step = head.next

        while single_step != double_step:
            if double_step == None or double_step.next == None:
                return False

            single_step = single_step.next
            double_step = double_step.next.next

        return True
