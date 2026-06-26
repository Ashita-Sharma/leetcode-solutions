# Description: Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Approach: Like all the other cases, we shall recurse to the bottom calculating the minimum depth along
# the way. However, there are four cases now. If the two children are null, we return zero. If only one
# child is present (either left or right) we return the depth of the null node. Similarly, when both nodes
# are present, we return the minimum value.

class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

#Time Complexity: O(n), we visit each node once
#Space complexity: O(h) height of the tree