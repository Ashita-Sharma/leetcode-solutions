#Description: Given a binary array nums, return the maximum number of consecutive 1's in the array.

#Approach: We can initialize a counter variable that updates number of ones seen so far, if current count is
#greater than maximum, update the maximum value. If we get a zero, reset the current count.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count

#Time Complexity: O(n)
#Space complexity: O(1)