#Description: You are given a license key represented as a string s that consists of only
#alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes.
#You are also given an integer k.
#We want to reformat the string s such that each group contains exactly k characters, except for the first
#group, which could be shorter than k but still must contain at least one character. Furthermore, there
#must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
#Return the reformatted license key.

#Approach: We turn the entire text into upper case and remove the dashes. Next we calculate the remainder
#of the length when we divide it by k. Next, if the modulo is zero, we can directly add the string
#divided into k length parts into a list. Otherwise, we can first append the remainder amount of characters
#from the start and then append rest of the characters.
# Finally, we join the string by using dashes and return it.


class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.upper()
        new_text = s.replace("-", "")
        first_len = len(new_text) % k
        if first_len != 0:
            chunks = []
            chunks.append(new_text[0:first_len])
            chunks += [new_text[i: i + k] for i in range(first_len, len(new_text), k)]
            string = "-".join(chunks)
            return string
        else:
            chunks = [new_text[i: i + k] for i in range(first_len, len(new_text), k)]
            string = "-".join(chunks)

            return string

#Time Complexity: O(n)
#Space complexity: O(n)