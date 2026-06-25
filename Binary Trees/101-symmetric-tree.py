# Description: Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
# symmetric around its center).

# Approach: For a mirrored tree, the left node of the left subtree will be the equivalent to the right node
# of the right subtree. Similarly, the right node of left subtree should be the same as the left node of
# right subtree. Furthermore, if both nodes are null, we can easily return true, however, if only one of
# them is null, we return false. Otherwise, we go deeper into the tree, checking the nodes until we reach
# the end (both nodes are null) or find a discrepancy.

class Solution:
    def isSymmetric(self, root):
        def is_mirror(n1, n2):
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)

        return is_mirror(root.left, root.right)

#Time Complexity: O(n)
#Space complexity: O(h)