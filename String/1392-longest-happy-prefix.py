# Description: A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
# Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

# Approach: Similar to problem 214, we use a rolling has to calculate the suffix and prefix in O(1) time.
# We are also mentioned that the suffix/prefix cannot be the string itself, hence, the suffix length is
# rejected if it reaches the length of the string itself. Otherwise, if suffix and prefix are equal, we
# update the value of the largest prefix. Finally, we return the value of the suffix.

class Solution:
    def longestPrefix(self, s):
        MOD = 10**9 + 7
        n = len(s)
        m = 0
        s_len = 0
        F = 0
        R = 0
        BASE = 31
        power = 1
        for k in range(len(s)):
            val_f = ord(s[k]) - ord('a') + 1
            val_r = ord(s[-1-k]) - ord('a') + 1
            F = (F * BASE + val_f) % MOD
            R = (R + val_r * power) % MOD
            power = (power * BASE) % MOD
            if F == R and k != n-1:
                m = k+1
        return s[0:m]


#Time Complexity: O(n)
#Space complexity: O(1)