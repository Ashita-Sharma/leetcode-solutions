#Description: Given the roots of two binary trees p and q, write a function to
#check if they are the same or not. Two binary trees are considered the same if they are structurally
#identical, and the nodes have the same value.

#Approach Description: Let us start from the root node, if at any point the two node values do not match,
#return false. Else, check the nodes of left and right subtree until the nodes point to null or the nodes differ.
#return true for the final case.

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False

#Time Complexity: O(n), where n is number of nodes
#Space complexity: O(h), for recursion