'''Description: You are given an integer array of unique positive integers nums. Consider the following graph:

There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.'''

'''Approach: Here, I used a modified union-find to keep the "parent" of every number cohesive.  The parents shall be
maintained using an array of size M+1(where M is the largest number in the array), with each number being its own parent initially. For a number, let's say 10,
all its factors(1,2,5) will also have their highest parent(either another number or itself) set to 10. This way, all connected 
numbers will eventually lead to the same number if we use the find function to recursively call its parent until
we reach the highest parent. To find the largest component, we can just maintain a dictionary of the frequency of each highest parent
(gotten from find(num)) and update the count. Then we can simply return the largest component size.'''


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent = list(range(max(nums) + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                parent[rootB] = rootA

        def primes_set(n):
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return primes_set(n // i) | set([i])
            return set([n])

        for num in nums:
            num_set = primes_set(num)
            for factor in num_set:
                union(num, factor)

        count = {}
        for num in nums:
            root = find(num)
            count[root] = count.get(root, 0) + 1
        return max(count.values())

#Time complexity: O(n)
#Space complexity: O(M)