'''Description: Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”'''

'''Approach: In a binary search tree, the smaller values are to the left, while the larger values are to the right.
Hence, when both values p and q are smaller, we know the LCA is also in the left subtree. If both the values are
greater, the LCA is to the right. We repeat this until both p and q are at the opposite sides of the current node.
Then, the current node is our answer. '''

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

#Time Complexity: O(H)
#Space complexity: O(1)