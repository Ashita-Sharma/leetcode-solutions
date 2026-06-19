#Description: Given a non-negative integer c, decide whether there're two integers a and b such
#that a2 + b2 = c.

#Approach: We let a take values in the range (0, sqrtC) as a^2 cannot exceed c. For each a we calculate
#the value of b and see if it is an integer. If yes, then we have got our pair. If we cannot find any pair,
#return false.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a * a)
            if b == int(b):
                return True
        return False

#Time Complexity: O(sqrtC)
#Space complexity: O(1)