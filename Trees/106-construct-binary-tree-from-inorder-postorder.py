# Description: Given two integer arrays inorder and postorder where inorder is the inorder traversal of
# a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

#Approach: First, we create a map of the index and value of the elements in the inorder form.
#For each node, we pick the last element in postorder, since postorder does left, right and root layout.
#With every node, we will recursively pop the root, find its index using the inorder map, and then
#recurse to create its left and right subtrees.

class Solution:
    def buildTree(self, inorder, postorder):
        in_map = {val: idx for idx, val in enumerate(inorder)}

        # Helper function to build tree recursively
        def build(l, r):
            if l > r:
                return None

            rootVal = postorder.pop()

            root = TreeNode(rootVal)

            inroot = in_map[rootVal]

            root.right = build(inroot + 1, r)
            root.left = build(l, inroot - 1)

            return root

        LastRoot = build(0, len(inorder) - 1)

        return LastRoot

#Time Complexity: O(n)
#Space complexity: O(n), due to recursion