#Description: Given the array nums after the possible rotation and an integer target,
#return the index of target if it is in nums, or -1 if it is not in nums.
#You must write an algorithm with O(log n) runtime complexity.

#Approach: Like ordinary binary search, we first calculate the middle index. If the lower index's element
#is less than the middle element, we can assume the left side to be sorted. Otherwise, we consider the
#right side to be sorted. Regardless, we check if target lies on the left side of the array, or not and
#work like a normal binary search.

class Solution:
    def search(self, nums, target):

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

#Time Complexity: O(logn)
#Space complexity: O(1)