#Description: Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points
# to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

#Approach: Let us store all the nodes in an array according to preorder traversal.
#Once we reach the end, let us remark the root node as the first index of the array.
#Then, we shall proceed normally, assigning the next node to current node's right until we reach the end.

class Solution:
    def flatten(self, root):
        self.q = []

        def preorder(node):
            if not node:
                return
            self.q.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        if self.q:
            self.q.pop(0)  # root will be reused
        while self.q:
            root.right = self.q.pop(0)
            root.left = None
            root = root.right

#Time Complexity: O(n)
#Space complexity: O(n), due to recursion