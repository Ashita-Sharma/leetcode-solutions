#There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is
#represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there
#is an edge between nodes ui and vi. Select any one node x at the maximum depth. Return the number of ways
#to assign edge weights in the path from node 1 to x such that its total cost is odd.
#Since the answer may be large, return it modulo 10^9+7.

#Approach Description: Use a dictonary or hashmap

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10 ** 9 + 7
        edges_map = {}

        for u, v in edges:
            if u not in edges_map:
                edges_map[u] = []
            edges_map[u].append(v)

            if v not in edges_map:
                edges_map[v] = []
            edges_map[v].append(u)

        def dfs(node, parent, depth):
            max_depth = depth

            for neighbor in edges_map[node]:
                if neighbor != parent:
                    max_depth = max(max_depth, dfs(neighbor, node, depth + 1))

            return max_depth

        max_depth = dfs(1, -1, 0)
        if max_depth == 0:
            return 0
        res = pow(2, max_depth - 1, MOD)
        return res

#Time Complexity: O(n)
#Space complexity: O(n)
