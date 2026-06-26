#Description: Given the root of a binary search tree, and an integer k, return the kth smallest
# value (1-indexed) of all the values of the nodes in the tree.

#Approach Description; We start from the smallest node, using inorder traversal (left, root, right).
#After we reach a node, we subtract 1 from k, and repeat until k reaches 0.
#At which point, the node we are on will be our answer.

class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            self.inorder(node.right)

#Time Complexity: O(N)
#Space complexity: O(H)