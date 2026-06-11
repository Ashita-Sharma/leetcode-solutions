#Description: Given an array of integers nums
#and an integer target, return indices of the two numbers such that they add up to target.

#Approach Description: Let us maintain a map (dictionary) of the current index and its corresponding value
#Similarly, as we iterate through the list we can calculate the required number to reach the target as well.
#If we find that the required number is already present in the mapping, we can return it's corresponding index
#As well as the index of the current number in the form of a list

class Solution:
    def twoSum(self, nums, target: int):
        mp = {}  # Dictionary to store element -> index
        for i, num in enumerate(nums):
            complement = target - num
            # If complement found, return indices
            if complement in mp:
                return [mp[complement], i]
            # Store current element and index
            mp[num] = i
        # No pair found
        return [-1, -1]

#Time Complexity: O(n)
#Space complexity: O(n)for the dictionary