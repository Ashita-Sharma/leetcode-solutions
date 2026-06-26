# Description: Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

# Approach: For each node in binary search tree, the center node between two subtrees is always the middle
# value. Then we separate the tree into left and right subtrees, for which the central node is again the
# middle value and so on until we reach the end of the subtree. This is a recursive format where we go from
# the top to the bottom.

class Solution:
    def sortedArrayToBST(self, nums):
        def convert(left, right):
            if left > right:
                return

            mid = (left + right) // 2

            node = TreeNode(nums[mid])

            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)

            return node

        return convert(0, len(nums) - 1)

#Time Complexity: O(n)
#Space complexity: O(n), due to recursion