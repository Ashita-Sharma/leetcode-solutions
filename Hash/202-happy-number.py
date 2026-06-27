# Description: Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Approach: The method for calculating the next number is fairly easy, by simply taking the remainder with
# 10, raising its power by 2 and dividing the number by 10 to get the next digit. We add the new numbers
# to a set. If a current number is in the set, we know the case will loop over and over again. Hence, we
# back out and return false.

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def get_next_number(n):
            res = 0

            while n:
                digit = n % 10
                res += digit ** 2
                n = n // 10

            return res

        while n not in visited:
            visited.add(n)
            n = get_next_number(n)
            if n == 1:
                return True

        return False

# Time Complexity: O(nlogn)
# Space complexity: O(n) for the set