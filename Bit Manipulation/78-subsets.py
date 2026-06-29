'''Description: Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.'''

'''Approach: We know that for a list of n numbers, the number of subsets are 2^(n-1). So, for each number in that 
range, we can take its bit value and if i is set (i == 1) then we know that number should be present in the current 
subset. For example, we have a list of [1,2,3] and the case will be 0, i.e. no numbers added. Next will be 1, which in
binary can be represented as 001, hence our next subset will be [3], for 5, its binary is 101 so the subset will be
[1,3] and so on and we append each subset to our final results list.'''

class Solution:
    def subsets(self, nums):
        n = len(nums)
        subsets = 1 << n

        ans = []

        for num in range(subsets):
            subset = []

            for i in range(n):
                if num & (1 << i):
                    subset.append(nums[i])
            ans.append(subset)

        return ans

#Time Complexity: O(N x 2^N)
#Space complexity: O(N x 2^N)