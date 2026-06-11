#Description: Given a binary array nums and an integer k, return the maximum number
#of consecutive 1's in the array if you can flip at most k 0's.

#Approach Description: Let us start from the leftmost element, increasing the window size towards the right by one,
#while keeping track of the number of zeroes within. If the number of zeros exceed the value of k. shrink
#the window until it is valid again, keeping track of the maximum window size.
#Return the answer after reaching the end.

class Solution:
    def longestOnes(self, nums, k):
        left = 0

        zeros = 0

        max_len = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

#Time Complexity: O(n)
#Space complexity: O(1) for constant variable