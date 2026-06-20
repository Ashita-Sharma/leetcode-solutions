#Description: An array nums of length n is beautiful if:
#nums is a permutation of the integers in the range [1, n].
#For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
#Given the integer n, return any beautiful array nums of length n.
#There will be at least one valid answer for the given n.

#Approach: First, let us understand the concept behind this array by using the smallest possible cases.
#For n = 1, the array will be [1], for n = 2, array will be [1,2]. For n=3, array will be [1,3,2].
#If we multiply it with 2, we get the even portion, and if we apply [x*2 -1], we get the odd portion.
#When we concatenate them both, we get the array of a 2y length. After this, we can simply pop the extra
#element until we get our desired length.

class Solution:
    def beautifulArray(self, n):
        init_array = [1,3,2]
        while len(init_array) < n:
            odd_part = [(x*2)-1 for x in init_array]
            even_part = [(x*2) for x in init_array]
            init_array = odd_part + even_part
        num = n+1
        while len(init_array) > n:
            idx = init_array.index(num)
            init_array.pop(idx)
            num += 1
        return init_array

#Note: For an O(n) time, we can replace both while loops with
        # while len(init_array) < n:
        #     odd_part = [2*x-1 for x in init_array if 2*x-1 <= n]
        #     even_part = [2*x for x in init_array if 2*x <= n]
        #     init_array = odd_part + even_part
        # return init_array
#Time Complexity: O(n^2)
#Space complexity: O(1)