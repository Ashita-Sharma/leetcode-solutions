'''Description: Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.'''

'''Approach: We only need to check how many patterns, out of the total patterns, appear at least once. Hence, if we
try to find a string in the word and it gives us an index (not -1) that means that string is in our word, hence we
increase the count.'''

class Solution:
    def numOfStrings(self, patterns, word):
        count = 0
        for s in patterns:
            if word.find(s) != -1:
                count += 1
        return count


#Time Complexity: O(n*m)
#Space complexity: O(1)