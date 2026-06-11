#Description: Given an unsorted integer array nums. Return the smallest positive integer
# that is not present in nums. You must implement an algorithm that runs in O(n) time
# and uses O(1) auxiliary space.

#Approach Description: Sort the array using a built-in sort for easier calculation.
#Next, starting the target with 1, iterate through the entire array, if current index is equal to target,
#Move on to the next index and increment the target by 1. If current target is not found, end the loop and
#return the target.

class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()

        target = 1
        for n in nums:
            if n > 0 and n == target:
                target += 1
            elif n > target:
                return target

        return target


#Time Complexity: O(nlogn)
#Space complexity: O(1) for constant variable