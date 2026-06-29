'''A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.'''

'''Approach: XOR lets us know how many bits are different in two numbers. So, we take XOR of both numbers, moving
from the right and checking if it is different i.e. its bit is 1, then we know it has to be flipped.'''

class Solution:
    def minBitFlips(self, start, goal):
        num = start ^ goal
        count = 0

        for i in range(32):
            count += (num & 1)

            num = num >> 1

        return count

#Time Complexity: O(1), bitwise operations take constant time and the loop happens for 32 bits.
#Space complexity: O(1)