#Description: Given a string s, find the length of the longest substring without duplicate characters.

#Approach Description: Here, we can use sliding window and a set that increases with
#each unique character towards the right and shrinks from the left with each repeating character.

#Key concept: Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s):
        left = max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

#Time Complexity: O(n), we interact with each character once
#Space complexity: O(1), constant space required for variables