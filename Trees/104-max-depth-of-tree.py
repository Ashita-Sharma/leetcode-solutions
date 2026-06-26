# Description: Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Approach: We perform depth first traversal, by recursively going deeper into the tree until we reach the
# leaf nodes. Then, we recurse back up, considering the maximum length from all the lengths of the child
# nodes, going up until we reach the root node, for which we add one unit to the final length. After the
# last recursion, the maximum answer is returned.

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#Time Complexity: O(n), we visit each node once
#Space complexity: O(h) height of the tree