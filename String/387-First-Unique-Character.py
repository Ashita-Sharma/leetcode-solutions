'''Description: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.'''

'''Approach: Let us simply keep a dictionary that has the character as key and a pair of index, frequency as its value.
Now as we iterate through the string, if a character is not already in the dictionary, we can add it as an element, marking
its first index and frequency. If it is already contained in the dictionary, we can simply increment the frequency.
In the end, we can just find the key character with a frequency of 1 and the smallest index and return it as the answer.'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        str_dict = {}

        for i in range(0, len(s)):
            char = s[i]
            if char not in str_dict:
                str_dict[char] = [i, 1]

            else:
                str_dict[char][1] += 1
        index = float('inf')
        for key, value in str_dict.items():
            if value[1] == 1 and value[0] < index:
                index = value[0]

        if index == float('inf'):
            return -1
        else:
            return index

#Time Complexity: O(n)
#Space complexity: O(n)

