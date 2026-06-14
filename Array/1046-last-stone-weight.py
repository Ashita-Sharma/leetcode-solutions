#Description: You are given an array of integers stones where stones[i] is the weight of the ith stone.
#We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them
#together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
#If x == y, both stones are destroyed, and
#If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
#At the end of the game, there is at most one stone left.
#
#Return the weight of the last remaining stone. If there are no stones left, return 0.

#Approach: We shall sort everything in decreasing order. Then we take the first two rocks, if both have
#equal weight, remove them both from the array. Otherwise, subtract the smaller weight and pop the smaller
#rock. Sort the array again due to changed weights. Return the value of the last stone.


class Solution:
    def lastStoneWeight(self, stones):
        stones.sort(reverse=True)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                stones[0] -= stones[1]
                stones.pop(1)
                stones.sort(reverse=True)
        if stones:

            return stones[0]
        else:
            return 0

#Time Complexity: O(nlogn) due to sorting
#Space complexity: O(1)