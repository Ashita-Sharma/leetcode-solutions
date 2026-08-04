'''Description: You are given an integer array nums consisting of unique integers.

Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.

The smallest and largest integers of the original range are still present in nums.

Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.'''

'''Approach: First we find the maximum and minimum value. The minimum will become our "curr" variable. While the curr
variable is not equal to largest, we will check if curr + 1 is in nums. If it isn't, we can append it to our result and
increment curr by 1. Then we finally return the result.'''

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        largest = max(nums)
        curr = min(nums)
        res = []
        while curr != largest:
            if curr + 1 not in nums:
                res.append(curr + 1)
            curr += 1

        return res

#Time complexity:O(n*r) where r is min(nums)-max(nums)
#Space complexity: O(1)