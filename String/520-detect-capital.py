#Description: We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

#Approach: Simply check if the entire word is lowercase, uppercase or titlecase and return the answer.

class Solution:
    def detectCapitalUse(self, word):
        if word.lower() == word:
            return True
        elif word.upper() == word:
            return True
        elif word.title() == word:
            return True
        else:
            return False

#Time Complexity: O(n)
#Space complexity: O(1)