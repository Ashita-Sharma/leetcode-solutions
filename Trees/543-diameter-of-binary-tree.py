'''Description: Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.'''

'''Approach: We start by moving from the deepest nodes(leaves). We keep track of the max size, whether that is our 
current result, or the sum of lengths left and right. Then, we move up, repeat the same process, and move up,
keeping all lengths maximum. For the result, we keep an outer variable res that we call with nonlocal res because 
global keyword looks for res in the outermost scope, while nonlocal looks for res in the scope just outside of it.'''


class Solution:
    def diameterOfBinaryTree(self, root):
        res = 0

        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            nonlocal res

            res = max(res, l + r)

            return 1 + max(l, r)

        dfs(root)
        return res

#Time Complexity: O(n)
#Space complexity: O(n)