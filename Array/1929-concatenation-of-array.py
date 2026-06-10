#Description: Given an integer array nums of length n, you want to create an array ans of length 2n where
# ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n

#Approach: For python, we can directly concatenate. Otherwise, we can create an array of length 2n, and add
#the element of index i at index i and i+n.

class Solution:
    def getConcatenation(self, nums):
        list1 = nums
        ans = list1 + nums
        return ans

#Time Complexity: O(n)
#Space complexity: O(1)