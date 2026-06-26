#Description: Given the root of a binary tree, return the level order traversal of its nodes' values.
#(i.e., from left to right, level by level).

#Approach Description: We start by creating a queue. We add the children of the current node in the queue and
#pop the first item, adding it to our result. Then, we take the first child, add its children to the queue,
#and move on to the next and so on until we have added all nodes to the result.


class Solution:
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans

#Time Complexity: O(n)
#Space complexity: O(n)