'''Description: Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

Return the kth bit in Sn. It is guaranteed that k is valid for the given n.'''

'''Approach: The binary string has the structure of (old string) + "1" + (old string with bits flipped). That means, 
the left and right halves are essentially mirror images of each other. Then, we can find the kth bit on the string by assuming 
where it is placed in the current string, then recurse back until we find it. If, for the current string, k is in the
left half, it's value will stay the same (not be inverted) and hence we can recurse to the n-1 case. If the k is in the
right half, we recurse to the n-1 case but flip the bit from 0 to 1 and vice versa. If k is the middle element(base case), we *know* it is
going to be 1 due to how the string is structured, so we can simply return 1 and recurse on the corresponding position in S(n-1). If we somehow reach n = 1, we know
the answer is 0, so we can return it as well.'''


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Edhe case: When n = 1, the binary string is "0"
        if n == 1:
            return '0'

        # Find the length of the current string Sn, which is 2^n - 1
        length = 2 ** n - 1

        # Find the middle position
        mid = length // 2 + 1

        # If k is the middle position, return '1'
        if k == mid:
            return '1'

        # If k is in the first half, find the bit in Sn-1
        if k < mid:
            return self.findKthBit(n - 1, k)

        # If k is in the second half, find the bit in Sn-1 and invert it
        return '1' if self.findKthBit(n - 1, length - k + 1) == '0' else '0'

#Time Complexity: O(n)
#Space complexity: O(n), due to recursion