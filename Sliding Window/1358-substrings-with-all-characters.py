#Description: Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

#Approach Description: Let us keep a hashmap that counts the frequency of a, b, c in the current substring.
#We can use sliding window to find an instance where all three characters are present in the substring. Then,
#this substring + any extension from the left will also be valid. Hence, we can find valid cases without
#recalculating everytime.

class Solution:
    def numberOfSubstrings(self, s):
        freq = [0, 0, 0]

        left = 0
        res = 0

        for right in range(len(s)):
            freq[ord(s[right]) - ord('a')] += 1

            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:

                res += len(s) - right

                freq[ord(s[left]) - ord('a')] -= 1
                left += 1

        return res


#Time Complexity: O(n)
#Space complexity: O(1)