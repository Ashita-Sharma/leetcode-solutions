'''Description: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.'''

'''Approach: First, we convert the array into a set. Now, while moving from left to right, if the predecessor of the 
current number is not in the array, we mark it as the start of the sequence. Then, we simply increase the length from 1 until
we reach the end of the sequence (current + 1 not in set) and then update the longest sequence. This way, we only
have to visit each element once and are checking in O(1) time due to hash set.'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                current = num

                while current + 1 in nums_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

#Time complexity:O(n)
#Space complexity: O(n)