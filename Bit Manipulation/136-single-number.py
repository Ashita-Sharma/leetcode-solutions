# Description: Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

#Approach Description: Here, we can use XOR function as the XOR of a number with itself is zero, and
#the XOR of a number with 0 is the number itself. Hence, all the duplicate numbers will have their XOR
#reduced to zero, and XOR of zero with the single number will be the number itself which is our answer.

class Solution:
    def singleNumber(self, nums):
        res = 0

        for n in nums:
            res ^= n

        return res


#Time Complexity: O(n)
#Space complexity: O(1)