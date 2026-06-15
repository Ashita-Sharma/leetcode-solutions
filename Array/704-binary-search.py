#Description: Given an array of integers nums which is sorted in ascending order, and an integer
#target, write a function to search target in nums. If target exists, then return its index.
#Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

#Approach: Binary search occurs in a sorted array. If the target is greater than the middle value, we can
#drop the smaller half. Otherwise, drop the greater half. Find the new middle, repeat the procedure until
#we find the target, otherwise return -1.


class Solution:
    def search(self, nums, target):
        n = len(nums)  # size of the array
        low = 0
        high = n - 1

        # Keep searching until low crosses high
        while low <= high:
            mid = (low + high) // 2  # Find the middle index
            if nums[mid] == target:
                return mid  # Target found
            elif target > nums[mid]:
                low = mid + 1  # Search in right half
            else:
                high = mid - 1  # Search in left half
        return -1  # Target not found

#Time Complexity: O(logn)
#Space complexity: O(1)