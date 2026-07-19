'''Description: You are given a string s and two distinct lowercase English letters x and y.

Rearrange the characters of s to construct a new string t such that:

t is a permutation of s.
Every occurrence of y appears before every occurrence of x in t.
Return any valid string t.

'''

'''Approach: We iterate through all characters in the given string. If the current character is not x, we simply append 
it directly to our answer. If it is x, we count the number of x seen in total and append x that many times to the end of
the answer.'''

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        x_count = 0
        ans = ""
        for char in s:
            if char != x:
                ans += char
            else:
                x_count += 1
        ans += x*x_count
        return ans

sol = Solution()
res = sol.rearrangeString(s = "axe", x = "o", y = "x")
print(res)