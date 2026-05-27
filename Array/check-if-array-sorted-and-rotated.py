# Given an array nums, return true if the array was originally sorted in
# non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.

#Approach Description: For a non-rotated array, we can just check if the current element is
# greater than the element before it. However, in a rotated array, there will be a point where
# there's a drop, i.e, where the current element is smaller than the previous.
# As such a scenario will only occur atmost once in a rotated array, we can count the number of drop(s)
# to get the answer.

class Solution:
    def check(self, nums):
        n = len(nums)

        drops = 0 #initialize the drop counter

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]: #allows it to act like a circular array
                drops += 1

        return drops <= 1 #returns answer in a boolean

#Time Complexity: O(n) iterating through each element once
#Space complexity: O(1) for the drop counter