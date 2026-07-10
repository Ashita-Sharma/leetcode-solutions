'''Description: Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.'''

'''Approach: First, we create a helper function to compute the result. The helper function gets the current character and
computes it based on the mentioned rules. If the current character is a digit, it is used to compute the number of times
the inner string will be repeated, if it is an open bracket [, we recurse inside to get the inner string and multiply it by the aforementioned number to get it repeated to the required number of times.
We run this loop until the character pointer (i) reaches the end of the string. Then we return the answer.'''

class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        return self.decode(s)
    def decode(self, s: str) -> str:
        res, num = "", 0
        while self.i < len(s):
            c = s[self.i]
            if c.isdigit():
                num = num * 10 + int(c)
                self.i += 1
            elif c == '[':
                self.i += 1
                inner = self.decode(s)
                res += inner * num
                num = 0
            elif c == ']':
                self.i += 1
                return res
            else:
                res += c
                self.i += 1
        return res

#Time Complexity: O(n)
#Space complexity: O(n), due to recursion

