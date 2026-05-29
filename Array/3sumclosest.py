#Description: Given an integer array nums of length n and an integer target,
# find three integers at distinct indices in nums such that the sum is closest to target.
# Return the sum of the three integers.

#Approach Description: Sort the array to make it easier to calculate. Use two pointers to create a three sum
#and calculate its absolute difference. Move over to the next region, calculate the difference which, if less
#than the current, is updated and so on, until we reach the end. Finally return the answer.
#Note: If we find a 3sum that is equal to the target we return target directly.

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(target - result):
                    result = total

                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result

#Time Complexity; O(n^2)
#Space Complexity: O(1)

