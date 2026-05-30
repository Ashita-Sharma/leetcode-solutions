#Description: Given two integers dividend and divisor, divide two integers without using multiplication,
# division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part.
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.

#Approach Description: First, we handle edge cases, i.e. when number is divided by one or the
# number itself, and so on. We find the sign of the final result. Then, we find the highest power of
# 2 such that the dividend can be subtracted by (divisor)*2^n. After subtracting the value, we repeat the same
# until the number cannot be subtracted by divisor itself.
# Our answer will be the sum of powers of 2.


class Solution:
    def divide(self, dividend, divisor):
        if dividend == divisor:
            return 1
        if dividend == -2 ** 31 and divisor == -1:
            return (2 ** 31) - 1
        if divisor == 1:
            return dividend

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        n, d = abs(dividend), abs(divisor)
        ans = 0

        while n >= d:
            p = 0
            while n >= (d << p):
                p += 1

            p -= 1
            n -= (d << p)
            ans += (1 << p)

        return min(max(sign * ans, -2 ** 31), 2 ** 31 - 1)

#Time Complexity: O((logn)^2) where n is the absolute value of dividend.
#Space complexity: O(1)