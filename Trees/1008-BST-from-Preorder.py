'''Description: Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.'''

'''Approach: We use a divide and conquer approach, dividing our array into left and right subparts, recursively
creating nodes through them over and over until we reach the leaf nodes.'''


class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None

        node = TreeNode(preorder[0])
        node.left = self.bstFromPreorder([x for x in preorder if x < preorder[0]])
        node.right = self.bstFromPreorder([x for x in preorder if x > preorder[0]])

        return node

#Time Complexity: O(N)
#Space complexity: O(N)

