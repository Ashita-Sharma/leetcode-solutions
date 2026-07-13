'''Description: An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.'''

'''Approach: For easy creation of numbers, I used a string of digits to compute the valid numbers. Similarly, I also converted
the low and high end numbers into strings as well. Then, depending on how large of a range is provided, a loop computes 
sequences by selecting a start point from the range of (1,10). For the required length, we take the part of the digit string
that has its starting at "start" and ends at "start+length". This way, we are able to compute sequences without handling digits.
If the current sequence is valid i.e. lies between low and high, we append it to our answer list.'''

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        s = "123456789"
        l = str(low)
        h = str(high)

        for length in range(len(l), len(h) + 1):
            for start in range(0, 10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans

# Time Complexity: O(1), maximum valid numbers are 36
# Space Complexity: O(1)