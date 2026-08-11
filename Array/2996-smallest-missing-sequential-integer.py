'''Description: You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.'''

'''Approach: First, we simply total the largest sequence we find starting from nums[0], breaking when the sequence breaks.
Then, we simply check if the number is in set(nums). If yes, we return, otherwise we check num+1.'''

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        seen = set(nums)

        answer = total

        while answer in seen:
            answer += 1

        return answer

#Time complexity: O(n)
#Space complexity: O(n)