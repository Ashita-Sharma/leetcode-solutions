# Description: You are given a string s. You can convert s to a palindrome by adding characters in front
# of it. Return the shortest palindrome you can find by performing this transformation.

# Approach: Here, we use hashing to store the forward hash as well as the reverse hash. If we consider the
# alphabet a-z to have values from 1-26 respectively, a string like "abc" will have the forward hash of
# 1*31**2 + 2*31 + 3 and a backward hash of 1 + 2*31 + 3*31**2. If both forward and backward hash are
# equal, we update the largest palindrome value. When we reach the end of the string, we take the
# characters that aren't in the palindrome, reverse them and add them to the start of the string.
# So a string like "aabcd" will have its palindrome be "dcbaabcd".

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        MOD = 10**9 + 7
        n = len(s)
        m = 0
        s_len = 0
        F = 0
        R = 0
        BASE = 31
        power = 1
        for char in s:
            s_len += 1
            value = ord(char) - ord('a') + 1
            F = (F * BASE + value) % MOD
            R = (R + value * power) % MOD
            power = (power * BASE) % MOD
            if F == R:
                m = s_len
        suffix = s[m:]
        res = suffix[::-1] + s

        return res

#Time Complexity: O(n)
#Space complexity: O(1)

