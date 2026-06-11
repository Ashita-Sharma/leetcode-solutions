#Description:You are given the root node of a binary search tree (BST) and a value to insert into the tree.
# Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.

#Approach Description: We start from the top, comparing the current node with the
#given value, moving left of given is smaller and moving right if given is greater, until we reach the end,
#where we insert the node into the correct position.

class Solution:
    def insertIntoBST(self, root, val: int):
        if root is None:
            return TreeNode(val)
        if root.val > val:
              root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

#Time Complexity: O(h), where h is height of the tree
#Space complexity: O(n), for an unbalanced tree