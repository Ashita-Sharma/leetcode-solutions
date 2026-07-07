'''Description: You are given an integer n.

Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.

Let sum be the sum of digits in x.

Return an integer representing the value of x * sum.'''

'''Approach: First, we initialize x and sum to be zero. We convert the number n into a string so we can traverse it
digit by digit without having to divide by 10 every time. We convert the non-zero digits into integers again,
concatenating them into x and adding them to the sum. Finally, we return sum*x.'''

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sum = 0
        n_str = str(n)
        for char in n_str:
            if char != "0":
                x = x*10 + int(char)
                sum += int(char)

        return x*sum

# Time Complexity: O(n)
# Space Complexity: O(1)