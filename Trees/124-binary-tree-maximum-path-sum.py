'''Description: A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.'''

'''Approach: Similar to 543, we take the maximum from each subtree as we move forward. However, here we sum the node
 values, rather than the distances themselves. For each node, we calculate the maximum sum using its children, then 
 we calculate their maximum by adding current node's value and so on until we reach the top node, where we finally
 return the maximum sum.'''


class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum

    def dfs(self, node):
        if not node:
            return 0

        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))

        self.max_sum = max(
            self.max_sum,
            left + right + node.val
        )

        return max(left, right) + node.val

#Time Complexity: O(n)
#Space complexity: O(n)