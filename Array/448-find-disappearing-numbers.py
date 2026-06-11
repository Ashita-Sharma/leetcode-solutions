#Description: Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the
#integers in the range [1, n] that do not appear in nums.

#Approach 1: We can create a set and iterate through it to find the missing number. Uses O(n) space and
#O(n) time.

#Approach 2: We can use the array itself to mark the indices seen already, making an index negative if we've
#seen its element already, for example, we mark the element of index 3 as negative if we have seen number 4
#already. Then, we iterate through the list again, adding the positive indexes to our missing list.

class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1

            if nums[idx] > 0:
                nums[idx] *= -1

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res

#Time Complexity: O(n)
#Space complexity: O(1)
