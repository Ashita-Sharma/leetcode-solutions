#Description: Given the root of a binary tree, return the postorder traversal of its nodes' values

#Approach Description: Similar to the previous two questions, we shall recursively reach the leftmost node,
#append the left node, move to the right node to append it, then append the parent node.
#recursively apply the same logic until all elements are traversed

#Key Concept: Postorder traversal uses Left, Right, Root traversal method.

class Solution:
    def postorderTraversal(self, root):
        res = []

        def postorder(root):
            if not root:
                return

            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res

#Time Complexity: O(n)
#Space complexity: O(n), due to recursion