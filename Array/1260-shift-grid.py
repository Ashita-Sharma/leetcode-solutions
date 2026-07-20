'''Description: Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.'''

'''Approach: The easiest way to solve is to simply convert the array into 1D, shift the array by k and convert it back 
into a 2D array. We can directly skip the second step by using a formula to find the correct position of the element after
shifting it k times. First, we find its 1D location which is i * n + j, then, we shift it by k, taking mod with the total to 
prevent exceeding it, then simply finding the new row and new column and placing the element in the correct position on
the answer grid.'''

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        total = m * n

        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                old_index = i * n + j

                new_index = (old_index + k) % total

                new_row = new_index // n
                new_col = new_index % n

                ans[new_row][new_col] = grid[i][j]

        return ans


#Time Complexity: O(n^2)
#Space complexity: O(1)