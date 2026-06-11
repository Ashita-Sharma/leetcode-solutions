#Description: Given the array nums, for each nums[i] find out how many numbers in the array are smaller
#than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and
#nums[j] < nums[i]. Return the answer in an array.

#Approach Description: If we sort the array, for any element X, the number of elements smaller than it will be
#index of the number X. Hence, we can just return the index of element X in the sorted array for each number.

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        return [sorted_nums.index(i) for i in nums]

#Time Complexity: O(nlogn)
#Space complexity: O(n)