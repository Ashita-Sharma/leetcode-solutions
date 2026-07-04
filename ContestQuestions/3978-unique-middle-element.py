'''Description: You are given an integer array nums of odd length n.

Return true if the middle element of nums appears exactly once in the array. Otherwise return false.'''

'''Approach: Simply keep track of the middle element's count. If its' count becomes greater than 1, return False.'''

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        middle = nums[len(nums) // 2]
        count = 0

        for num in nums:
            if num == middle:
                count += 1

        return count == 1

# Time Complexity: O(n)
# Space Complexity: O(1)