'''
414. Third Maximum Number
Easy

818

1471

Add to List

Share
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:

Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        import sys
        nums = list(set(nums))
        maxnum = nums[0]
        max_2nd = max_3rd= -sys.maxsize
        
        if len(nums)>1:
            i=1
            while(i<len(nums)):
                if maxnum < nums[i]:
                    previous_maxnum = maxnum
                    maxnum = nums[i]
                else:
                    previous_maxnum = nums[i]
                if len(nums) > 2: 
                    if max_2nd < previous_maxnum:
                        previous_max_2nd = max_2nd
                        max_2nd = previous_maxnum
                    else:
                        previous_max_2nd = previous_maxnum
                    if max_3rd < previous_max_2nd:
                        max_3rd = previous_max_2nd
                        
                i += 1
        
        if (len(nums) < 3):
            return maxnum
        else:
            return max_3rd
