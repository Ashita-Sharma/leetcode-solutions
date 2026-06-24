# Description: Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Approach: We can make a hashmap of values we have seen before and their index. For each value we come
#across while iterating, we check if it is a duplicate. If yes, we check if the distance between the indices
#is less than k. If yes, we return True, otherwise we add it to the visited hashmap. If by the end of the
#iteration we have not gotten our answer, we return false.

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        visited = {}

        for i, val in enumerate(nums):
            if val in visited and i - visited[val] <= k:
                return True
            else:
                visited[val] = i

        return False

#Time Complexity: O(n)
#Space complexity: O(n)for the dictionary