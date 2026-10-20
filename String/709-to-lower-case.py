'''Description: Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.'''

'''Approach: Instead of using any built in functions, we can simply see if the ASCII value of the character is between 65 and 90 (ie uppercase),
If yes, we can simply update its value to be original value + 32 to convert it into lowercase and repeat for all characters.'''

class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for ch in s:

            if 65 <= ord(ch) <= 90:
                result += chr(ord(ch) + 32)
            else:
                result += ch

        return result

#Time Complexity: O(n)
#Space complexity: O(1)