'''Description: You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].

For each queries[i], extract the substring s[li..ri]. Then, perform the following:

Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
Let sum be the sum of digits in x. The answer is x * sum.
Return an array of integers answer where answer[i] is the answer to the ith query.

Since the answers may be very large, return them modulo 109 + 7.'''

'''Approach: I used the concept of cumulative values in this question. First, I created arrays that will store the number of 
digits seen so far, sum of digits as well as another that will store the actual number created in the window [0, i]. The sum is straightforward enough 
for the window between l, r -- simply take sum[r] - sum [l] to get the sum. However, for getting the actual number, we do
num[r] - num[l] * POW, where POW is 10 raised to the power of the difference between them. For example, if [l,r] is
[2,4], we raise the num ber at index 2 to the power of r - l, which is 2 here, so the number becomes R - L*100 to remove the digits before 2.'''

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # idx[i] = number of non-zero digits before index i
        idx = [0] * (n + 1)

        # val[i] = number formed by first i non-zero digits
        val = [0] * (n + 1)

        # total[i] = sum of first i non-zero digits
        total = [0] * (n + 1)

        cnt = 0

        for i, ch in enumerate(s):
            digit = int(ch)

            if digit != 0:
                cnt += 1
                val[cnt] = (val[cnt - 1] * 10 + digit) % MOD
                total[cnt] = total[cnt - 1] + digit

            idx[i + 1] = cnt

        ans = []

        for l, r in queries:

            left = idx[l]
            right = idx[r + 1]

            # No non-zero digit in the range
            if left == right:
                ans.append(0)
                continue

            length = right - left

            number = (val[right] - val[left] * pow10[length]) % MOD
            sum_digits = total[right] - total[left]

            ans.append((number * sum_digits) % MOD)

        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)