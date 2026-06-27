# Description: You are given an array of positive integers nums.
#
# You need to select a subset of nums which satisfies the following condition:
#
# You can place the selected elements in a 0-indexed array such that it follows the pattern: [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x] (Note that k can be be any non-negative power of 2). For example, [2, 4, 16, 4, 2] and [3, 9, 3] follow the pattern while [2, 4, 8, 4, 2] does not.
# Return the maximum number of elements in a subset that satisfies these conditions.

# Approach: In the worst case possible, the maximum array will be formed of 1s, as 1 to any power is still
# 1. Hence, when we first initialize the result, we take the maximum odd count of 1s present. In that vein,
# We initialize a frequency array that contains the frequency of all elements. Then, while we iterate
# through all elements, we should realise that other than the highest element, we only need 2 members of
# each value. If the sqrt of the current element already has 2+ members in our frequency table we know that
# whatever subset we create is already included in the previous one, hence we skip. Otherwise, we check if
# current element **2 exists and its frequency and so on until we get element**2 element whose frequency is
# 1. After which we calculate the max length and return it when we reach the end of our iteration.


class Solution:
    def maximumLength(self, nums):
        freq = Counter(nums)
        ones = freq.pop(1, 0) - 1
        if ones % 2 == 0:
            res = ones +1
        else:
            res = ones
        for f in freq:
            x = f
            sq = isqrt(x)
            if sq * sq == x and freq.get(sq, 0) > 1:
                continue

            n = 0
            while x <= 31622 and freq.get(x, 0) > 1:
                n += 2
                x *= x

            if x in freq:
                total = n + 1
            else:
                total = n - 1
            res = max(res, total)
        return res

#Time Complexity: O(n)
#Space complexity: O(n) for the hash array