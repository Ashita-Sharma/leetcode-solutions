'''Description: Given string num representing a non-negative integer num, and an integer k, return the
 smallest possible integer after removing k digits from num.'''

'''Approach: We maintain a stack that keeps track of smallest elements we come across and update it
 with each new element. If the topmost element is greater than the current digit, we pop it and add the new digit.
After k is zero, we directly push all digits to the stack. If the stack is full but we still have k elements left to 
be removed, we simply pop k elements from the stack and join our answer(removing any leading zeroes).'''

class Solution:
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        stack = stack[:-k] if k > 0 else stack

        result = ''.join(stack).lstrip('0')
        return result if result else '0'

#Time Complexity: O(n)
#Space complexity: O(n), because of stack