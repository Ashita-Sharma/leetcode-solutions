'''Description: You are given two non-negative integers n and s.

Return the largest integer that has at most n digits and whose sum of digits is s. If no such integer exists, return -1.'''

'''Approach: To get the maximum possible integer, the digits going from left to right have to be the largest possible as well.
Case 1: If the required sum is less than 10, we can make the leftmost digit the sum itself and fill rest values with 0 until we reach a length of n.
Case 2: Otherwise, if the sum is greater than 9, we can simply keep adding 9 to our number and decreasing the remaining sum by 9 until its count is in single digits, and then the process is same as Case 1.
Finally, we can convert the string into integer and return the answer.'''

class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        sum_remaining = s
        res = ""
        while sum_remaining != 0:
            if sum_remaining > 9:
                res += "9"
                sum_remaining -=9
            else:
                res += str(sum_remaining)
                sum_remaining -= sum_remaining
        if len(res) > n:
            res = "-1"
        elif len(res)< n:
            res += "0"*(n-len(res))

        return int(res)

#Time complexity:O(k), where k is s/n (number of times the while loop will trigger)
#Space complexity: O(1), no extra space required
