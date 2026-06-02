#Description:Given two strings s and t of lengths m and n respectively, return the minimum window
#substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

#Approach Description: let us create a dictionary of all required letters and their frequencies.
#then, we shall calculate the minimum length required. Initialize Left and right pointers and result length.
#If current length less than required, we shall increase the window to the right by one.
#If all required characters with their respective frequencies are in this window, we shall compare it to our
#current result length and update accordingly.
#Return the result after reaching the end.

from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not t:
            return ""
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        left = 0

        res = [-1, -1]
        res_len = float("inf")

        for right in range(len(s)):

            char = s[right]

            window[char] = 1 + window.get(char, 0)

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:

                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = [left, right]

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1
        if res_len == float("inf"):
            return ""

        return s[res[0]:res[1] + 1]