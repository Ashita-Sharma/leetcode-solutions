#Description: Given the root of a binary tree, return the preorder traversal of its nodes' values.

#Approach Description: Preorder traversal is known as depth-first traversal, hence we shall
#start by traversing until we reach the leftmost node, append its parent to the list, add it to the list,
#go up one level to its parent, go to its right child, add it to the list and recursively
#apply this method until we reach have traversed each element once.

#Key Concept; Inorder traversal uses Root, Left, Right traversal method.
class Solution:
    def preorderTraversal(self, root):
        res = []

        def preorder(node):
            if not node:
                return

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return res

#Time Complexity: O(n)
#Space complexity: O(n), due to recursion