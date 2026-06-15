#Description: A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and
#B are valid parentheses strings, and + represents string concatenation.
#Return s after removing the outermost parentheses of every primitive string in the primitive
#decomposition of s.

#Approach: Let us initialize a level counter. It increases with every "(" and decreases with every ")".
#If the level is 0, we know we are at the outermost parentheses so we do not need to add them to
#our result. We add all the rest and return the string.

class Solution:
    def removeOuterParentheses(self, s):
        # Initialize result string
        result = ""
        # Initialize nesting level counter
        level = 0

        # Traverse the string
        for char in s:

            if char == '(':

                if level > 0:
                    result += char

                level += 1
            elif char == ')':

                level -= 1

                if level > 0:
                    result += char

        # Return the final result
        return result

#Time Complexity: O(n)
#Space complexity: O(1)