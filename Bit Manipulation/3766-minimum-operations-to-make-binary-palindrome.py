'''Description: You are given an integer array nums.

For each element nums[i], you may perform the following operations any number of times (including zero):

Increase nums[i] by 1, or
Decrease nums[i] by 1.
A number is called a binary palindrome if its binary representation without leading zeros reads the same forward and backward.

Your task is to return an integer array ans, where ans[i] represents the minimum number of operations required to convert nums[i] into a binary palindrome.'''

'''Approach: Since all constraints are less than 5000, we can simply precompute every single binary palindrome, store it in an
array and use it to find the nearest palindromic number. Then we simply need to return the minimum value difference between
given number and the palindrome. For this, we can use the built-in bisect function to find the closest palindromic value.
Then we simply compare the difference between the closes match and the one before it to find the minimum difference. Then we
append all values and return the result.'''

class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        pal = []
        for x in range(1, 5001):
            b = bin(x)[2:]
            if b == b[::-1]:
                pal.append(x)

        ans = []
        for x in nums:
            idx = bisect_left(pal, x)

            best = float('inf')

            if idx < len(pal):
                best = min(best, abs(x - pal[idx]))

            if idx > 0:
                best = min(best, abs(x - pal[idx - 1]))

            ans.append(best)

        return ans

#Time complexity:O(n)
#Space complexity: O(n)