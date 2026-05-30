#Description: Given the root of a binary tree, return the inorder traversal of its nodes' values.

#Approach Description: Like how we approached preorder traversal recursively, we shall apply the same concept
#here. First we shall traverse to reach the leftmost node, add it to the list, backtrack to its parent
#add its parent to the list and then traverse to its right sibling.

#Key Concept: Inorder traversal uses Left, Root, Right traversal method


class Solution:
    def inorderTraversal(self, root):
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

#Time Complexity: O(n)
#Space complexity: O(n), due to recursion