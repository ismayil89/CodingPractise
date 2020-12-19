"""
LeetCode - 448
Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing_items = []
        for i in nums:
            if nums[abs(i) - 1] > 0:
                nums[abs(i) - 1] = -nums[abs(i) - 1]

        for i in range(len(nums)):
            if nums[i] > 0:
                missing_items.append(i + 1)
        return missing_items
