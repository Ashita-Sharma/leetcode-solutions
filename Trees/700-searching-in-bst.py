# Description: You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the
# subtree rooted with that node. If such a node does not exist, return null.

#Approach Description: We know that in a Binary Search Tree the numbers smaller
#than the current node are to its left, while the greater values are too its right.
#Hence, we shall use this approach to compare current node's value to key value until we either find the node
#or the tree ends.

class Solution:
    def searchBST(self, root, val):
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


#Time Complexity: O(h), where h is height of the tree
#Space complexity: O(n), for an unbalanced tree
