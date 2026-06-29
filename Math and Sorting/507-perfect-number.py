''' Description: A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.'''

'''Approach: We know for every number greater than 1, it will have 1 ass its divisor. Then, we check every number 
in the range 2, num/2 (as the largest divisor can only be num /2) to see if the remainder of num with another number,
say i, is zero. If yes, we add the quotient of num divided by i to our result.'''

class Solution:
    def checkPerfectNumber(self, num):
        if num==1:
            return False
        count=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                count+=i+num//i
        return num==count

#Time Complexity: O(n/2)
#Space complexity: O(1)