#Description: Given an array of positive integers nums, remove the smallest subarray (possibly
#empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the
#whole array. Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
#A subarray is defined as a contiguous block of elements in the array.

#Approach: Sum the entire array and find out the remainder that we need to remove from the array.
#If the remainder is 0, we can return 0 directly. Otherwise, we iterate through the array, having created
#a hashmap. Then, we can create the prefix remainder, checking if the other needed value (to get the
#remainder to 0) is in the map, if yes, we update the minimum answer with the new subarray length.
#Otherwise, if we do not find a valid subarray, we return -1.

class Solution:
    def minSubarray(self, nums, p):
        target = sum(nums)%p
        if target == 0:
            return 0
        mp = {0: -1}
        prefix = 0
        ans = len(nums)

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p
            need = (prefix - target) % p

            if need in mp:
                ans = min(ans, i - mp[need])

            mp[prefix] = i
        if ans == len(nums):
            return -1
        return ans


#Time Complexity: O(n)
#Space complexity: O(1)
