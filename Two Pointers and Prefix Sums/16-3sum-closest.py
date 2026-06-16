#Description: Given an integer array nums of length n and an integer target, find three integers at
#distinct indices in nums such that the sum is closest to target.
#Return the sum of the three integers.

#Approach: Start by sorting the array to make calculations easier. We start by calculating the smallest
#possible sum and label it result. Then, we increment ahead and see if the current three sum is closer
#to target than the old sum and update accordingly. The 3sum is calculated by adding the current element,
#the element after it and the last element. If the total sum is less than target, we know to move to
#the larger element. #Otherwise, if the sum is greater, we go to a smaller element and repeat until we
#have received our answer


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

#Time Complexity: O(n^2)
#Space complexity: O(1)