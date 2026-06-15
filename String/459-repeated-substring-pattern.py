#Description:Given a string s, check if it can be constructed by taking a substring of it and
#appending multiple copies of the substring together.

#Approach: There are two end cases possible, either the first character is copied through the entire string
#and the case where the first half of the string is copied to create the final string. Hence, we only need
#check till the middle of the string. Hence, we start by checking the smallest possible answer and if
#the substring multiplied to the length of the actual string is the same as the original string, we
#return true. Otherwise, if we complete the entire loop, we know the answer is false.

class Solution:
    def repeatedSubstringPattern(self, s):
        length = len(s)
        for i in range(1, length // 2 + 1):
            if length % i == 0 and s[:i] * (length // i) == s:
                return True

        return False

#Time Complexity: O(n)
#Space complexity: O(1)