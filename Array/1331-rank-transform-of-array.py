'''Description: Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.'''

'''Approach: First, I copy the original array to a second variable and sort it in ascending order. Then, after 
initializing the first rank as 1 and creating a hashmap for ranks, I iterate through all numbers in the sorted array.
If the number is not already present in the hashmap, give it the current rank, add it to the hashmap and increase the current 
rank to 1. Then, for all numbers present in the original array, we simply swap the current  number for its corresponding rank
in the map.'''

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)

        rank = {}
        current_rank = 1

        for num in sorted_arr:
            if num not in rank:
                rank[num] = current_rank
                current_rank += 1

        return [rank[num] for num in arr]

#Time Complexity: O(nlogn) due to sorting
#Space complexity: O(n)