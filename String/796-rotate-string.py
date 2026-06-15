#Description:Given two strings s and goal, return true if and only if s can become goal after
#some number of shifts on s.
#A shift on s consists of moving the leftmost character of s to the rightmost position.

#Approach: If the given string and goal are not the same length, the rotation is not possible so
#we immediately return false. Otherwise, we double the string. Now this doubled string contains all
#possible cases of the rotated string. Hence, we can return true if goal is in string and false otherwise.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        doubled_s = s + s
        return goal in doubled_s

#Time Complexity: O(n)
#Space complexity: O(n)