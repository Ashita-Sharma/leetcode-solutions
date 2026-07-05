'''Description: You are given an integer array nums.

The digit range of an integer is defined as the difference between its largest digit and smallest digit.

For example, the digit range of 5724 is 7 - 2 = 5.

Return the sum of all integers in nums whose digit range is equal to the maximum digit range among all integers in the array.'''

'''Approach: First, I create a helper function that calculates the digit range in O(n) time. Then, I iterate for each
number in nums to see if its range is equal to the current max range. If yes, update the total sum. If its range
is greater, update the sum and the max range. Finally, return the answer.'''

class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def digit_range(num):
            digits = [int(d) for d in str(num)]
            return max(digits) - min(digits)
        max_range = 0
        ans = 0
        for num in nums:
            d_range = digit_range(num)
            if d_range > max_range:
                max_range = d_range
                ans = num
            elif d_range == max_range:
                ans += num
            else:
                continue
        return ans

# Time Complexity: O(n**2)
# Space Complexity: O(k) where k is the maximum number of digits