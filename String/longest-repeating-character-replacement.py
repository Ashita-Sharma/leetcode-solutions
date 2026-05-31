#Description:You are given a string s and an integer k. You can choose any character of the string and
# change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing
# the above operations.

#Approach Description: Let us maintain a hashmap of the element with the highest frequency.
#Expanding our window towards the right, let us continue updating the frequency.
#If the number of replacements exceed the value of K, shrink the window size from the left.
#Continue until we reach the end of the array.

class Solution:
    def characterReplacement(self, s, k):
        freq = {}

        left = 0

        max_freq = 0

        max_len = 0

        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1

            max_freq = max(max_freq, freq[s[right]])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

#Time Complexity: O(n)
#Space complexity: O(1)