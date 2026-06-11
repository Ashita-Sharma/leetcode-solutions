#Description: Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

#Approach Description: First, to handle edge cases, if number of rows = 1 or greater than number of letters,
#return the string itself. Else, initialize the first index of the row and the direction.
#The direction will mark whether we need to go down while writing zigzag or go up.
#Finally, append all letters into the final, concatenated string.

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)

#Time Complexity: O(n) for iterating through arrays
#Space complexity: O(1) for array and creating string