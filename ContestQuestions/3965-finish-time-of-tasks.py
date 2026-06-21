# Description: You are given an integer n representing the number of tasks in a project, numbered from 0 to n - 1. These tasks are connected as a tree rooted at task 0. This is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that task ui is the parent of task vi.
#
# You are also given an array baseTime of length n, where baseTime[i] represents the time to complete task i.
#
# The finish time of each task is calculated as follows:
#
# Leaf task: The finish time is baseTime[i].
# Non-leaf task:
# Let earliest be the minimum finish time among its children, and latest be the maximum finish time among its children.
# Let ownDuration be (latest - earliest) + baseTime[i].
# The finish time of task i is latest + ownDuration.
# Return the finish time of the root task 0.

#Approach: Similar to question 3558, we use a storage structure to store the relationship between nodes.
#A node's value is based on the earliest and latest time of its children as well as its own base time
#based on the provided formula. Hence, every time we reach a node, we can update its time in the baseTime
#array by the following structure. We start with the depth first order, for each node, calculating the
#baseTimes for its children recursively. Finally, we return the base time of node 0.

class Solution:
    def finishTime(self, n: int, edges, baseTime):
        children = [[] for _ in range(n)]

        for u, v in edges:
            children[u].append(v)

        def dfs(node):
            if not children[node]:
                return baseTime[node]

            child_times = []

            for child in children[node]:
                child_times.append(dfs(child))

            earliest = min(child_times)
            latest = max(child_times)

            ownDuration = (latest - earliest) + baseTime[node]

            return latest + ownDuration

        return dfs(0)

#Time Complexity: O(n)
#Space complexity: O(n) due to recursion