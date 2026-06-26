# Description:  Given a binary tree, determine if it is height-balanced.

# Approach: Here, let us imagine starting from the leaf nodes of the subtrees, we compare their lengths
# to see if they are balanced and then go up, taking the maximum height from each case. If at any point
# the tree is not balanced, we get false. We calculate absolute difference for ease of calculation as we
# recurse upwards.

class Solution:
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True, 0]

            left_balanced, left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)

            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return [is_balanced, 1 + max(left_height, right_height)]

        return dfs(root)[0]

#Time Complexity: O(n), we visit each node once
#Space complexity: O(n)