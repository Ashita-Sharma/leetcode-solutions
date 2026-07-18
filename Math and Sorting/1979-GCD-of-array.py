'''Description: Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.'''

'''Approach: We know that the we can find the GCD of an array of numbers by simply calculating the GCD of the largest and 
the smallest number. For ease of calculation, we can use the euclidian algorithm. For the euclidian algorithm, we take the
form a = b*q + r, where a is the larger number, b is the divisor, q is the quotient and r is the remainder.
After we get the value of r, we replace a with b and b with r, we repeat this until the remainder becomes zero, after which our 
current divisor is the GCD.'''

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b

        return a

    def findGCD(self, nums: List[int]) -> int:

        minimum = min(nums)

        maximum = max(nums)

        return self.gcd(minimum, maximum)

#Time Complexity: O(n)
#Space complexity: O(1)