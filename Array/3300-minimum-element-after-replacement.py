# Description: You are given an integer array nums.
# You replace each element in nums with the sum of its digits.
# Return the minimum element in nums after all replacements.

#Approach Description: Initialize the minimum value. While iterating through the array, calculate the sum
#and continuously update the smallest value found. Upon reaching the end of the array, print the final minimum value.


class Solution:
    def minElement(self, nums):
        min_val = float('inf')

        for num in nums:
            current_sum = 0

            while num > 0:
                current_sum += num % 10
                num //= 10

            min_val = min(min_val, current_sum)

        return min_val

#Time Complexity: O(n*log10(M)) for calculating sum of digits
#Space complexity: O(1) for constant variable