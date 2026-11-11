'''Description: Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.'''

'''Approach: First, we convert entire string into a list for easy modifications. In the first pass, we make a list of vowels that appear in the string
and reverse it. Then, in the second pass, we take the original string, check if the current character is a vowel and replace it with the reversed vowel.
Finally, we join the string and return the result.'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AaEeIiOoUu"
        char_list = []
        s_list = list(s)
        for char in s_list:
            if char in vowels:
                char_list.append(char)
        char_list.reverse()
        cur_i = 0
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = char_list[cur_i]
                cur_i += 1

        return "".join(s_list)

#Time Complexity: O(n) n being length of string
#Space complexity: O(m) m being number of vowels