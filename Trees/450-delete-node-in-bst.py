#Description: Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.

#Approach Description: There are three possible cases for deleting a node.
#1) Leaf node -> delete directly
#2) Only one child -> replace with child
#3) Both children -> replace with left child, attaching the right child to it's rightmost node


class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.val == key:
            return self.helper(root)

        dummy = root
        while root is not None:
            if root.val > key:
                if root.left is not None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return dummy

    def helper(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        rightChild = root.right
        lastRight = self.flr(root.left)  # rightmost node in left subtree
        lastRight.right = rightChild
        return root.left

    def flr(self, root):
        if root.right is None:
            return root
        return self.flr(root.right)

#Time Complexity: O(h)
#Space complexity: O(1)