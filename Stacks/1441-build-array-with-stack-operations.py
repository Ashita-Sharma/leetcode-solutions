#Description: You are given an integer array target and an integer n. Return the stack operations needed to
#build target following the mentioned rules. If there are multiple valid answers, return any of them.

#Approach Description: There are three possible cases that can happen, as we iterate through the numbers
#from 1 to n.
#Case 1: Number in the list, push it directly.
#Case 2: Number not in list but smaller than last element of target, push and pop to remove it and move to
#the next number in the stream
#Case 3: Number not in list and greater than last element of target, no need to do anything, either pass
#or break the loop.

class Solution:
    def buildArray(self, target, n):
        res = []
        for i in range(1, n+1):
            if i in target:
                res.append("Push")
            elif i > target[-1]:
                pass
            else:
                res.append("Push")
                res.append("Pop")
        return res

#Time Complexity: O(n)
#Space complexity: O(1)