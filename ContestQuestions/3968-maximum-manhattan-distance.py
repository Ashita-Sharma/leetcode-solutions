# Description: You are given a string moves consisting of the characters 'U', 'D', 'L', 'R', and '_'.
# Starting from the origin (0, 0), each character represents one move on a 2D plane:
# 'U': Move up by 1 unit.
# 'D': Move down by 1 unit.
# 'L': Move left by 1 unit.
# 'R': Move right by 1 unit.
# '_': Can be independently replaced with any one of 'U', 'D', 'L', or 'R'.
# Return the maximum Manhattan distance from the origin that can be achieved after all moves have been performed.

#Approach: Take two variables to mark the x and y coordinates respectively. Here, I chose a list with two
#elements, one for x-axis and one for y-axis. We can easily create the logic for moving up, down, left,
#right. For the _, we can intuitively understand that for each _ there must be at least one direction where
#the resulting overall length will be increased by 1. Hence, when we calculate the final manhattan distance
#which is just displacement in x + displacement in y, we add the extra length as well.

class Solution:
    def maxDistance(self, moves: str) -> int:
        coord = [0, 0]
        extra = 0

        for char in moves:
            if char == "L":
                coord[0] -= 1
            elif char == "R":
                coord[0] += 1
            elif char == "U":
                coord[1] += 1
            elif char == "D":
                coord[1] -= 1

            else:
                extra += 1

        ans = abs(coord[0]) + abs(coord[1]) + extra
        return ans

#Time Complexity: O(n) where n is length of moves
#Space complexity: O(1)