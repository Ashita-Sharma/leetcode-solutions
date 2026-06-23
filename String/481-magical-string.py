# Description: A magical string s consists of only '1' and '2' and obeys the following rule:
#
# Concatenating the sequence of lengths of its consecutive groups of identical characters '1' and '2' generates the string s itself.
# The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and counting the occurrences of 1's or 2's in each group yields the sequence "1 2 2 1 1 2 1 2 2 1 2 2 ......".
#
# You can see that concatenating the occurrence sequence gives us s itself.
#
# Given an integer n, return the number of 1's in the first n number in the magical string s.

#Approach: From the pattern example we can see that every last digit is the opposite of the previous group.
#If previous was 2, then we take 1 and vice versa. The frequency of the appended element is the last value
#of the last index visited. Next, we increment the pointer by 1. When the length is greater than n, we
#return the count of 1s in the result.

class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            s += [3 - s[-1]] * s[i]
            i += 1
        return s[:n].count(1)

#Time Complexity: O(n)
#Space complexity: O(n) for the string