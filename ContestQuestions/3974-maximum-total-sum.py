'''You are given an integer array nums and two integers k and mul.

Select exactly k elements from nums. Process these elements one by one in any order you choose.

For each selected element, independently choose one of the following:

Add the element's value to the total sum, or
Multiply the element by the current value of mul and add the result to the total sum.
After processing each selected element, mul decreases by 1, regardless of which option was chosen. The current value of mul may become 0 or negative.

Return an integer denoting the maximum possible total sum.'''

'''Approach: First, let us sort all numbers in reverse order. Then, taking the first k numbers, if they are
positive, we multiply them by mul. Otherwise, we divide them by mul and add the resultant to our answer.'''

class Solution:
    def maxSum(self, nums, k, mul):
        nums.sort(reverse=True)
        res = 0
        for num in nums[0:k]:
            if mul > 1:
                res += num*mul
                mul -= 1
            else:
                res += num
                mul -= 1
        return res

#Time Complexity: O(nlogn) due to sorting
#Space complexity: O(1)