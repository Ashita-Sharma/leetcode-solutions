#Description: You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.
# Build a new string result by processing s according to the following rules from left to right:
# If the letter is a lowercase English letter append it to result.
# A '*' removes the last character from result, if it exists.
# A '#' duplicates the current result and appends it to itself.
# A '%' reverses the current result.
# Return the final string result after processing all characters in s.

#Approach: First, we initialize an empty string to hold our answer. Next, we iterate through every
#character in the string. If the character is "*", we remove the last element, if it is "#" we append
#the result to itself and if it is "%" we reverse the result. Otherwise, the character will be an alphabet
#which we can append directly.

class Solution:
    def processStr(self, s):
        res = ""
        for char in s:
            if char == "*":
                res = res[:-1]
            elif char == "#":
                res += res
            elif char == "%":
                res = res[::-1]
            else:
                res += char
        return res

#Time Complexity: O(n)
#Space complexity: O(1)