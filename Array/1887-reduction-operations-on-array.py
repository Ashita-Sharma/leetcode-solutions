#Description: Given an integer array nums, your goal is to make all elements in nums equal.
#To complete one operation, follow these steps:
#Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
#Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
#Reduce nums[i] to nextLargest.
#Return the number of operations to make all elements in nums equal.

#Approach: In a reverse sorted array, for each new element we see, we know that we have to convert all
#previous numbers to the current number. Hence the count of operations increases by 1.

class Solution:
    def reductionOperations(self, nums):
        nums.sort(reverse = True)
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += i
        return count

#Time Complexity: O(n)
#Space complexity: O(1)