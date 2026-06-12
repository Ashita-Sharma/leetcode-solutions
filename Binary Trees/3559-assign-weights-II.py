#Description:There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The
#tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates
#that there is an edge between nodes ui and vi. You are given a 2D integer array queries. For each
#queries[i] = [ui, vi], determine the number of ways to assign weights to edges in the path such that the
#cost of the path between ui and vi is odd.

#Approach Description: The steps are as follows- 1) Use Depth First Search to compute the depth of each node
#from root node(node 1). 2) Then use the jump-up function to jump in powers of 2(binary lifting) until their
#parent node is the same(LCA). 3) Use the formula distance(1,u) + distance(1,v) - 2*distance(1, LCA) to find
#distance between the two nodes. 4) Finally, use the formula 2**(distance-1) to compute all possible cases.

#Binary lifting: For binary lifting, lift the deeper node until we get both nodes to the same depth.
#If the nodes at this point are the same, the highest node is the LCA. Otherwise, take the highest power of 2
#jump that is possible without reaching the same node. Repeat until the parents are the same. That parent node
#is your LCA.

class Solution:
    MOD = 10**9 + 7

    def modPow(self, a, b):
        ans = 1

        while b > 0:
            if b & 1:
                ans = (ans * a) % self.MOD

            a = (a * a) % self.MOD
            b >>= 1

        return ans

    def dfs(self, node, parent):
        self.up[node][0] = parent

        for j in range(1, self.LOG):
            self.up[node][j] = self.up[self.up[node][j - 1]][j - 1]

        for neighbour in self.adj[node]:
            if neighbour == parent:
                continue

            self.depth[neighbour] = self.depth[node] + 1
            self.dfs(neighbour, node)

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]

        for j in range(self.LOG - 1, -1, -1):
            if diff & (1 << j):
                u = self.up[u][j]

        if u == v:
            return u

        for j in range(self.LOG - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]

        return self.up[u][0]

    def assignEdgeWeights(self, edges, queries):
        n = len(edges) + 1

        self.LOG = 1
        while (1 << self.LOG) <= n:
            self.LOG += 1

        self.adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

        self.depth = [0] * (n + 1)
        self.up = [[0] * self.LOG for _ in range(n + 1)]

        self.dfs(1, 0)

        ans = []

        for u, v in queries:
            L = self.lca(u, v)

            dist = self.depth[u] + self.depth[v] - 2 * self.depth[L]

            if dist == 0:
                ans.append(0)
            else:
                ans.append(self.modPow(2, dist - 1))

        return ans

#Time Complexity: O(nlogn)
#Space complexity: O(nlogn)