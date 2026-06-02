#Description: You are given an integer array nums. You are initially positioned at the array's first index, and each
# element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

#Approach Description: let us start from the back going checking if it is possible to reach the last
# index via the second index. If possible, we go back to previous and see if it is possible to reach
# the second index (new goal) and repeat until we reach the first index of the array.
# If at any point it is not possible, return false.

class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False

#Time Complexity: O(n)
#Space complexity: O(1)