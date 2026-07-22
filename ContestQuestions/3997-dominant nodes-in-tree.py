'''Description: You are given the root of a complete binary tree.

A node x is called dominant if its value is equal to the maximum value among all nodes in the subtree rooted at x.

Return the number of dominant nodes in the tree.'''

'''Approach: For this, we can simp;y use a depth-first traversal to recursively get the maximum value for each subtree,
checking if it is greater than root-val and updating our count accordingly.'''

class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count = 0

        def postorder(root):
            nonlocal count

            if not root:
                return float("-inf")

            left_max = postorder(root.left)
            right_max = postorder(root.right)

            subtree_max = max(root.val, left_max, right_max)

            if root.val == subtree_max:
                count += 1

            return subtree_max

        postorder(root)
        return count

#Time Complexity: O(n)
#Space complexity: O(n)