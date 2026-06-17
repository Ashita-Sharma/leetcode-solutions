#Description: You are given an integer array nums. You can choose exactly one index (0-indexed)
#and remove the element. Notice that the index of the elements may change after the removal.
#An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.
#Return the number of indices that you could choose such that after the removal, nums is fair.

#Approach: First we calculate the entire sum of odd elements and the even elements. We take the left sums
#and right sums to have a boundary based on the element we removed. When we remove an element, the right
#sums switch roles, odd_right becomes even_right and vice versa. Next, we check if left+right sums are
#equal, and update the count. Then, we add the current removed element to left_odd, if its index is odd,
#left_even otherwise. Finally, after iterating through all values, we return the answer.

class Solution:
    def waysToMakeFair(self, nums):
        odd_right = 0
        even_right = 0
        for odd in range(1, len(nums), 2):
            odd_right += nums[odd]
        for even in range(0, len(nums), 2):
            even_right += nums[even]
        even_left = 0
        odd_left = 0
        ans = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even_right -= nums[i]
                new_even = even_left + odd_right
                new_odd = odd_left + even_right
                if new_even == new_odd:
                    ans += 1
                even_left += nums[i]
            else:
                odd_right -= nums[i]
                new_even = even_left + odd_right
                new_odd = odd_left + even_right
                if new_even == new_odd:
                    ans += 1
                odd_left += nums[i]
        return ans

#Time Complexity: O(n)
#Space complexity: O(1)
