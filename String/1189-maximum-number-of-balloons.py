# Description: Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

#Approach: In the word "balloon", the letters l and o appear twice as many times as the letters b, a and n.
#Hence, we can traverse the string counting the occurrences of each letter and return the value that
#appears the least amount of times.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = a = l = o = n = 0

        for c in text:
            if c == 'b':
                b += 1
            elif c == 'a':
                a += 1
            elif c == 'l':
                l += 1
            elif c == 'o':
                o += 1
            elif c == 'n':
                n += 1

        return min(b, a, l // 2, o // 2, n)

