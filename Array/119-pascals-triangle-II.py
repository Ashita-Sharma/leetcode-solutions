# Description: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Approach: First, we should know that the code below is the same as how we work on pascals' triangle on
# paper: padding the edges with 1, adding pairs of elements together and adding them to the row and so on
# until we reach our required row index. Here, we use the zip() function to convert our previous row
# into tuples of two for ease of calculation. However, since the ending 1's do not have anyone to pair
# with, we let them pair with zeros, one for the start and one for the end. This for loop runs until
# we reach our row number.

class Solution:
    def getRow(self, rowIndex: int):
        row = [1]

        for _ in range(rowIndex):
            row = [left + right for left, right in zip([0] + row, row + [0])]

        return row

#Time Complexity: O(n**2) where n is the size of rowindex
#Space complexity: O(n)