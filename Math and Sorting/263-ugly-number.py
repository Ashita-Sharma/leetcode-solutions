# Description: An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

# Approach: Simply just loop the values 2,3,5 until we have exhausted all possible divisions. If, after
# dividing the number multiple times by 2,3,5 until its no longer divisible, its value is equal to one, we
# know it has no other factors and hence is an ugly number. Otherwise, if it is not equal to one, it has
# more factors, hence we return false.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        for factor in [2,3,5]:
            while n%factor ==0:
                n//=factor
        return n==1

#Time Complexity: O(logn) due to repeated division
#Space complexity: O(1)