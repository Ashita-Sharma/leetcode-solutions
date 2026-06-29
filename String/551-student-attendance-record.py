'''Description: You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.'''

'''Approach: Highly straightforward. We simply keep track of total As seen so far as well as total consecutive Ls
seen so far. If we encounter a character that is not L, we reset its count. If L or A count reach the threshold,
We break out of  the loop and return False.'''

class Solution:
    def checkRecord(self, s) :
        l_count = 0
        a_count = 0

        for char in s:
            if char == "L":
                l_count +=1
                if l_count == 3:
                    return False
            elif char == "A":
                a_count += 1
                if a_count == 2:
                    return False
                l_count = 0
            else:
                l_count = 0
        return True

#Time Complexity: O(n)
#Space complexity: O(1)