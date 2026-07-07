'''Description: You are building a string s of length n one character at a time, prepending each new character to the front of the string. The strings are labeled from 1 to n, where the string with length i is labeled si.

For example, for s = "abaca", s1 == "a", s2 == "ca", s3 == "aca", etc.
The score of si is the length of the longest common prefix between si and sn (Note that s == sn).

Given the final string s, return the sum of the score of every si.'''

'''Approach: I used the Z-algorithm. First, I initialize a Z-array of length n, where Z[i] stores the length of the 
longest prefix of the string that matches the substring starting at index i. I also maintain a Z-box [L, R], 
which represents the current segment known to match the prefix. If the current index lies outside the Z-box, 
I compute the match length manually using a while loop and update the Z-box if a longer matching segment is found.
 If the current index is inside the Z-box, I initialize its Z-value using the minimum of the corresponding 
 previously computed Z-value (Z[i - L]) and the remaining length of the Z-box. If this match reaches the end of 
 the Z-box, I continue comparing characters with the while loop to see if the match can be extended further. 
 Finally, I sum all the values in the Z-array and add n, since the entire string matches itself.'''


class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        Z = [0] * n # initializing an n elements long empty list
        L = R = 0

        for i in range(1, n):
            if i <= R: # inside z-box
                Z[i] = min(R - i + 1, Z[i - L]) # minimum matching characters

            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]: # if characters match, increase the z list value
                Z[i] += 1

            if i + Z[i] - 1 > R: # if new box found
                L = i # update box boundaries
                R = i + Z[i] - 1

        return n + sum(Z)

#Time Complexity: O(n)
#Space complexity: O(n)