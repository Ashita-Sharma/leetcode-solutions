'''Description: You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots. Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the
flowerbed without violating the no-adjacent-flowers rule and false otherwise.'''

'''Approach: For each index, we can check its left and right pots. If both are 0, we can plant it here and our n
count goes down. If we cant, we skip it. We return a check for whether we got n down to zero or less. However, there
are two edge cases, i = 0 and i = length - 1. For these two cases, we consider our of bound points to be unplanted'''


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[ i -1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[ i +1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0

#Time Complexity: O(n)
#Space complexity: O(1)