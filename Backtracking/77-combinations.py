'''Description: Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.'''

'''Approach: We use backtracking in this question. In theory, we first take one number, add it to our combinations, and then branch
out using all possible cases from there on out. For example, if we have the numbers [1,2,3,4] and we need to make combinations
of size 2, we take 1, and then pair it with one of the remaining possible numbers(for example, 2), and since it reached our required
size, we add it to our result. Then, we remove the last element (2) and add the next number (3), and repeat until we get all pairs in the 
form of [1, num]. Then, we remove 1, and instead replace it with 2 and repeat the same process over and over until we get our required elements.
However, we also need to prevent duplicates like [1,2] and [2,1]. Hence, we give the helper function a start index value to keep track
of which elements we need to use and which we have to skip. Finally, we return the results as a list.'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return

            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()

        backtrack(1)
        return res

#Time Complexity: O(n*k)
#Space complexity: O(k)