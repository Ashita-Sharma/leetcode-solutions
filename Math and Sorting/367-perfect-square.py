'''Description: Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.'''

'''Approach: We can maintain a simple binary search, from 2, to half of the number itself, as it's square root cannot be 
larger than that. Then, we simply decrease the size of the search space, shifting to the left or right of the searchspace depending
on whether the squared value is greater or less than the number provided. If left = right, then we have reached the end of the
 search without finding the value. Hence, the given number is not a perfect square.'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid
            if squared == num:
                return True
            elif squared < num:
                left = mid + 1
            else:
                right = mid - 1

        return False

#Time Complexity: O(logn) binary search time complexity
#Space complexity: O(1)