'''Description: You are given two integer arrays start and target, where each array is of the form [x, y] representing a cell on a standard 8 x 8 chessboard.

Return true if a knight can move from start to target in an even number of moves. Otherwise, return false.'''

'''Approach: We know that in a chessboard, the a knight always lands on the same color it started on *if* the number 
of moves is even. Hence, we can simply calculate its final position color and its initial position color and check if it is the same.
Since a chessboard's colors alternate, and it's color can be mathematically determined by (x + y) % 2, we can just use
this formula to find if both values for target and start are equal.'''

class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2


#Time Complexity: O(1)
#Space complexity: O(1)