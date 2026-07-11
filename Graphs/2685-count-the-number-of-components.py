'''Description: You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices'''

'''Approach: (DFS) First, we create a hashmap of all the vertices mentioned in the given data. We also initialize a list of 
size n that will keep track of all the vertices we have or have not visited yet. Then, for each vertice in our hashmap
that we have not yet visited, we calculate the number of its neighbours(edges) and through it whether its a connected
component with all others present (checking if E = V(V-1) where E and V are total accumulated Edges and Vertices respectively).
If yes, we increase our res count by 1 (adding 1 each time we get another entirely connected vertice). '''


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        A = defaultdict(list)
        for u, v in edges:
            A[u].append(v)
            A[v].append(u)

        vis, res = [False] * n, 0
        for i, state in enumerate(vis):
            if not state:
                D = V = 0

                def dfs(x):
                    nonlocal V, D
                    V += 1
                    D += len(A[x])
                    vis[x] = True

                    for state in A[x]:
                        if not vis[state]:
                            dfs(state)

                dfs(i)
                res += D == V * (V - 1)

        return res

# Time Complexity: O(n+m)
# Space Complexity: O(n+m)