'''Description: A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.'''

''' Approach 1: Intuitive
Given the constraints are =< 100, we don't need to optimize and can simply use the easiest method, computing all possible
strings and returning the kth string. For this, we shall use the classic backtracking algorithm to compute one string, 
add it to our list of combinations, remove the last element, compute the next string and repeat until we get all possible
combinations. To maintain lexographical order, we keep a set of the valid characters in alphabetical order and compute
the valid strings in that order itself. In order to prevent same consecutive characters, the backtrack function also takes in
the last character as a parameter as well to check if the current character and the previous one are different. Finally,
we return Kth element.

Optimization 1: Only keep track of combinations until it is k elements long, and then return the last combination.

Optimization 2: Instead of an actual array, keep track of the combinations count incrementing by 1 every time we get a valid
string and when the count is equal to k, return that combination.
'''


class Solution: # BASIC
    def getHappyString(self, n: int, k: int) -> str:
        char_set = ["a", "b", "c"]
        combinations = []
        s = []

        def makestr(s, last_char):
            if len(s) == n:
                combinations.append("".join(s))
                return

            for char in char_set:
                if char != last_char:
                    s.append(char)
                    makestr(s, char)
                    s.pop()

        makestr(s, "z")
        if len(combinations) < k:
            return ""
        return combinations[k - 1]


class Solution: # OPTIMAL
    def getHappyString(self, n: int, k: int) -> str:
        char_set = ["a", "b", "c"]
        count = 0
        combinations = []
        s = []

        def makestr(s, last_char):
            if len(s) == n:
                nonlocal count
                count += 1
                if count == k:
                    return "".join(s)
                combinations.append("".join(s))
                return

            for char in char_set:
                if char != last_char:
                    s.append(char)
                    res = makestr(s, char)
                    if res:
                        return res
                    s.pop()

        ans = makestr([], "")
        return ans if ans else ""

#Time Complexity: O(1), because the total maximum possible cases within the constraints are 1536, which is a small constant
#Space complexity: O(1)