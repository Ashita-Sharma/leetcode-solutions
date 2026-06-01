#Description: Given the root of a binary tree, determine if it is a valid binary search tree (BST).

#Approach Description: Let us follow inorder traversal, if current value less than or equal to previous value,
#return false, otherwise true.
class Solution:
    def isValidBST(self, root):
        self.prev = float('-inf')

        def inorder(node):
            if not node:
                return True

            if not inorder(node.left):
                return False

            if node.val <= self.prev:
                return False

            self.prev = node.val

            return inorder(node.right)

        return inorder(root)

#Time Complexity: O(N)
#Space complexity: O(H)