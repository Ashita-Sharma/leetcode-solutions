#Description: You are given a positive integer n.
# Let digitSum be the sum of the digits of n, and let squareSum be the sum of the squares of the digits of n.
# An integer is called good if squareSum - digitSum >= 50.
# Return true if n is good. Otherwise, return false.

#Approach: Quite straightforward, simply calculate the sum of digits and sum of square of digits and
#apply the condition.

class Solution:
    def checkGoodInteger(self, n):
        digitSum = sum(int(digit) for digit in str(n))
        squareSum = sum((int(digit)**2) for digit in str(n))
        diff = squareSum - digitSum
        return diff >= 50

#Time Complexity: O(n)
#Space complexity: O(1)