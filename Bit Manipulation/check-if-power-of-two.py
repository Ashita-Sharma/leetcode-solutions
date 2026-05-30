# Description: Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

#Approach Description: We know that the bitwise AND for a number that is the power of two and the number
#just before it is 0. Hence, we can easily return true if the number is greater than 0 and
#their bitwise AND is also equal to zero.

class Solution:
    def isPowerOfTwo(self, n):
        return (n > 0 and (n & (n - 1))== 0)

#Time Complexity: O(1), bitwise operations take constant time
#Space complexity: O(1)