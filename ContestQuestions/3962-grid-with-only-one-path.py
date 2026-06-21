# Description: You are given two integers m and n, representing the number of rows and columns of a grid.

# Construct any m x n grid consisting only of the characters '.' and '#', where:
#
# '.' represents a free cell.
# '#' represents an obstacle cell.
# A valid path is a sequence of free cells that:
#
# Starts at the top-left cell (0, 0).
# Ends at the bottom-right cell (m - 1, n - 1).
# Moves only:
# Right, from (i, j) to (i, j + 1), or
# Down, from (i, j) to (i + 1, j).
# Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

#Approach: We know we can return any pattern that can only contain one path from (0,0) to (m,n). Hence,
#let us take one horizontal line of "."s, from (0,0) to (0,m) and a vertical line of "."s from (0,m) to
#(n,m). For this, we first fill an entire array of n x m with "#"s and replace them with "."s based on the
#above condition. Since we need an array of strings instead of a nested array, we join each row
#into a string.

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = [['#'] * n for _ in range(m)]

        for j in range(n):
            res[0][j] = '.'

        for i in range(m):
            res[i][n - 1] = '.'

        return [''.join(row) for row in res]

#Time Complexity: O(mn)
#Space complexity: O(1)