'''Description: You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.'''

'''Approach: Since the constraints are very small, we can easily calculate every simgle number rather than trying to derive a
more complex formula. We check if current number's product of digits is divisible by the given number. If not, we move
on to the next number and so on until we get our answer.'''

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            x = n

            while x > 0:
                product *= x % 10
                x //= 10

            if product % t == 0:
                return n

            n += 1

#Time complexity: O(t) in the worst possible case we will have to reach the number itself
#Space complexity: O(1)