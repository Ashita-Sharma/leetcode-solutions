#Description: You are given a string s consisting of lowercase English letters and the special
#characters: '*', '#', and '%'.
#You are also given an integer k.
#Return the kth character of the final string result. If k is out of the bounds of result, return '.'.

#Approach: First, let us process the length of resulting string at each character. If the current
#character is "#" length doubles, if it is "*", length is reduced by 1 and so on and append each updated
#length to a list.
#Now, if k is greater than the final length, we know it will have an index out of range so we directly
#return. Otherwise, we iterate through in reverse order. If the current character index is equal to k,
#and not a special character, we know we can return this character directly. Otherwise, we compute the
#updated location of k based on the special character we encountered. If the character doubles the length,
#as we go back we will reduce k by that factor. If the character is "%", we will take consider k to be
#taken from the opposite side and so on until we get k to be the index of the last element.

class Solution:
    def processStr(self, s, k):
        n = len(s)
        ln = 0
        lengths = []
        for char in s:
            if char == '*':
                ln = max(ln - 1, 0)
            elif char == '#':
                ln *= 2
            elif char != "%":
                ln += 1
            lengths.append(ln)

        if k >= ln:
            return "."

        for i in range(n - 1, -1, -1):
            char = s[i]
            if char == "#":
                if k >= lengths[i] // 2:
                    k -= lengths[i] // 2
            elif char == "%":
                k = lengths[i] - 1 - k
            elif char == "*":
                continue
            else:
                if lengths[i] == k + 1:
                    return char

#Time Complexity: O(n)
#Space complexity: O(n)