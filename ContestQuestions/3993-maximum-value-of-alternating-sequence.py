'''Description: You are given three integers n, s, and m.

A sequence seq of integers of length n is considered valid if:

seq[0] = s.
The sequence is alternating, meaning that either:
seq[0] > seq[1] < seq[2] > ..., or
seq[0] < seq[1] > seq[2] < ....
For every adjacent pair, |seq[i] - seq[i - 1]| <= m.
A sequence of length 1 is considered alternating.

Return the maximum possible element that can appear in any valid sequence.'''

'''Approach: Consider the first element to be s, then to get a maximum value in the end, the next value should be s+m,
the third value shall be s+m-1 (largest minimum value) and the fourth value shall be s+2m-1, the fifth will be
s+2m-1 and so on. Hence, we can directly derive the formula for the maximum value as ans = s + m +(p-1)*(m - 1), where 
p = n//2.'''

class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        p = n//2
        ans = s + m +(p-1)*(m - 1)
        if n == 1:
            return s
        else:
            return ans


sol = Solution()
res = sol.maximumValue(n = 4, s = 3, m = 5)
print(res)

#Time Complexity: O(1)
#Space complexity: O(1)