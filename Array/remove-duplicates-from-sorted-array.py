# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
# such that each unique element appears only once.
# The relative order of the elements should be kept the same.

#Approach Description: We iterate through all elements, remembering the position of the last unique element
#when we find the next unique element, we write its value onto the next index.
#we then increment the position of the last unique value by one.
#we repeat until we reach the end of the array.

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        write = 1  # position to write next unique value

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write

#Time Complexity: O(n)
#Space complexity: O(1) for a constant variable "write"
