#Description:Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
# such that adding up all the values along the path equals targetSum. A leaf is a node with no children.

#Approach Description: First, we initialize base case, if root does not exist, any traversal is impossible.
#Hence, we return false. Now, if the node is a leaf node, we check if it's pathSum matches the target.
#Otherwise, we subtract the current node's value from the target to reduce the target and make calculating easier.
#Then, we recursively call left and right subtrees until we find the correct leaf node.

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum - root.val == 0

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

#Time Complexity: O(n)
#Space complexity: O(n), due to recursion
